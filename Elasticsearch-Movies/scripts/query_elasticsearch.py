#!/usr/bin/env python3
"""
Script para consultar datos de Elasticsearch y prepararlos para visualización.
"""

import json
import pandas as pd
from elasticsearch import Elasticsearch
import os

def get_elasticsearch_data():
    """Obtener datos de Elasticsearch si está disponible. Usa fallback local si falla."""
    
    # 1. Intentar conexión y consulta
    try:
        cloud_id = os.getenv('ELASTICSEARCH_CLOUD_ID')
        username = os.getenv('ELASTICSEARCH_USERNAME') 
        password = os.getenv('ELASTICSEARCH_PASSWORD')
        
        if cloud_id and username and password:
             # Conexión en entorno de GitHub Actions
            es = Elasticsearch(
                cloud_id=cloud_id,
                http_auth=(username, password)
            )
        else:
            # Conexión local
            es = Elasticsearch(['http://localhost:9200'])
            
        if es.ping():
            # Consultar todos los documentos (máx 100 hits para evitar errores de tamaño)
            result = es.search(
                index="movies-tarea989", 
                body={"query": {"match_all": {}}, "size": 100}
            )
            
            # Convertir a DataFrame
            hits = result['hits']['hits']
            movies = [hit['_source'] for hit in hits]
            print(f"✅ Datos obtenidos de Elasticsearch: {len(movies)} documentos.")
            return pd.DataFrame(movies)
            
    except Exception as e:
        print(f"⚠️  No se pudo obtener datos de Elasticsearch ({e}). Usando datos locales como fallback.")
    
    # 2. Fallback: datos locales
    try:
        with open('data/movies.json', 'r', encoding='utf-8') as f:
            movies = json.load(f)
        print(f"⚠️ Datos locales cargados: {len(movies)} documentos.")
        return pd.DataFrame(movies)
    except Exception as e:
        print(f"❌ ERROR FATAL: Fallo al cargar el fallback local: {e}")
        return pd.DataFrame()
