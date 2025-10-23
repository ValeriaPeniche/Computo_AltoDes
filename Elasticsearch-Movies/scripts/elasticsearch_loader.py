#!/usr/bin/env python3
"""
Script que carga datos a Elasticsearch Cloud.
"""

import json
import os
from elasticsearch import Elasticsearch
import pandas as pd

# Nota: El mapping debe reflejar que 'genre' es una lista, por lo que usaremos 'keyword'
# para que se pueda filtrar, y 'actors' es un texto/lista.

def connect_elasticsearch():
    """Conectar a Elasticsearch Cloud o local."""
    try:
        # 1. Variables de entorno (usadas por GitHub Actions)
        cloud_id = os.getenv('ELASTICSEARCH_CLOUD_ID')
        username = os.getenv('ELASTICSEARCH_USERNAME') 
        password = os.getenv('ELASTICSEARCH_PASSWORD')
        
        if cloud_id and username and password:
            es = Elasticsearch(
                cloud_id=cloud_id,
                http_auth=(username, password)
            )
        else:
            # 2. Fallback para desarrollo local (si no hay variables)
            print("⚠️ Usando conexión local (http://localhost:9200)")
            es = Elasticsearch(['http://localhost:9200'])
            
        if es.ping():
            print("✅ Conectado a Elasticsearch")
            return es
        else:
            print("❌ Error: No hay conexión a Elasticsearch")
            return None
            
    except Exception as e:
        print(f"❌ Error conectando a Elasticsearch: {e}")
        return None

def load_sample_data():
    """Cargar datos de muestra desde archivo JSON"""
    # Asegúrate de que el path sea correcto desde la raíz del proyecto
    file_path = 'data/movies.json' 
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    """Función principal que carga los datos."""
    print("🚀 Iniciando carga de datos a Elasticsearch...")
    
    es = connect_elasticsearch()
    
    if es:
        index_name = "movies-tarea989"
        
        # Eliminar y crear índice
        if es.indices.exists(index=index_name):
            es.indices.delete(index=index_name)
            
        mapping = {
            "mappings": {
                "properties": {
                    "title": {"type": "text"},
                    "genre": {"type": "keyword"}, # Usamos keyword para listas de texto
                    "year": {"type": "integer"},
                    "duration": {"type": "integer"},
                    "rating": {"type": "float"},
                    "director": {"type": "keyword"},
                    "actors": {"type": "keyword"}
                }
            }
        }
        es.indices.create(index=index_name, body=mapping)
        
        # Cargar datos
        movies = load_sample_data()
        for i, movie in enumerate(movies):
            # Cuidado: El ID debe ser una cadena para ES
            es.index(index=index_name, id=str(i+1), document=movie)
            
        es.indices.refresh(index=index_name) # Asegura que los datos sean visibles de inmediato
        print(f"✅ {len(movies)} películas cargadas en Elasticsearch")
        
    else:
        print("🛑 Detenido. No se pudo conectar a Elasticsearch. Revisa tus Secrets o conexión local.")

if __name__ == "__main__":
    main()
