#!/usr/bin/env python3
"""
Script que conecta y carga el dataset de películas a Elasticsearch Cloud.
"""

import json
import os
from elasticsearch import Elasticsearch

# La ruta del archivo JSON debe ser relativa a donde se ejecuta el script (Elasticsearch-Project/)
DATA_PATH = '../data/movies.json'
INDEX_NAME = "movies-tarea989"

def connect_elasticsearch():
    """Conectar a Elasticsearch Cloud o local."""
    try:
        # Usamos variables de entorno (Secrets de GitHub)
        cloud_id = os.getenv('ELASTICSEARCH_CLOUD_ID')
        username = os.getenv('ELASTICSEARCH_USERNAME') 
        password = os.getenv('ELASTICSEARCH_PASSWORD')
        
        if cloud_id and username and password:
            # Conexión a Elasticsearch Cloud (en GitHub Actions)
            es = Elasticsearch(
                cloud_id=cloud_id,
                http_auth=(username, password),
                request_timeout=30 # Aumentar timeout por si la conexión es lenta
            )
        else:
            # Fallback para desarrollo local (con Docker o ES local)
            print("⚠️ WARNING: Usando conexión local (http://localhost:9200) o credenciales faltantes.")
            es = Elasticsearch(['http://localhost:9200'])
            
        if es.ping():
            print("✅ Conectado a Elasticsearch")
            return es
        else:
            print("❌ ERROR: Elasticsearch no responde (ping fallido)")
            return None
            
    except Exception as e:
        print(f"❌ ERROR conectando a Elasticsearch: {e}")
        return None

def load_sample_data():
    """Cargar datos de muestra desde archivo JSON"""
    try:
        # La ruta es relativa al directorio 'scripts'
        with open(DATA_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ ERROR: Archivo de datos no encontrado en {DATA_PATH}")
        return []

def main():
    """Función principal que carga los datos."""
    print("🚀 Iniciando carga de datos a Elasticsearch...")
    
    es = connect_elasticsearch()
    
    if es:
        # 1. Crear/recrear índice con mapping
        if es.indices.exists(index=INDEX_NAME):
            es.indices.delete(index=INDEX_NAME)
            
        mapping = {
            "mappings": {
                "properties": {
                    "title": {"type": "text"},
                    "genre": {"type": "keyword"}, # Para arrays y conteo
                    "year": {"type": "integer"},
                    "duration": {"type": "integer"},
                    "rating": {"type": "float"},
                    "director": {"type": "keyword"},
                    "actors": {"type": "keyword"}
                }
            }
        }
        es.indices.create(index=INDEX_NAME, body=mapping)
        print(f"✅ Índice '{INDEX_NAME}' creado.")
        
        # 2. Cargar datos
        movies = load_sample_data()
        if not movies:
            return

        for i, movie in enumerate(movies):
            # Usar 'document' en lugar de 'body' para versiones recientes
            es.index(index=INDEX_NAME, id=str(i+1), document=movie)
            
        es.indices.refresh(index=INDEX_NAME) 
        print(f"✅ {len(movies)} películas cargadas y refresco de índice completado.")
        
    else:
        print("🛑 Proceso detenido. No se pudo conectar a Elasticsearch.")

if __name__ == "__main__":
    main()

