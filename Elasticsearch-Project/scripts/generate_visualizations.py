#!/usr/bin/env python3
"""
Script para generar visualizaciones (gráficos) con Matplotlib/Seaborn y guardarlas para GitHub Pages.
Incluye depuración para GitHub Actions y fallback de datos de prueba.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
import query_elasticsearch  # Script de consulta a ES

# Ruta de salida de los gráficos (docs/assets en la raíz del repo)
OUTPUT_DIR = '../../docs/assets'
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_visualizations():
    """Consulta datos de ES y genera gráficos PNG."""
    print("Generando visualizaciones...")

    # Obtener datos desde Elasticsearch
    df = query_elasticsearch.get_elasticsearch_data()

    # Depuración: imprimir info del DataFrame
    if df is not None:
        print(f"DEBUG: Número de filas obtenidas de Elasticsearch: {len(df)}")
        print(df.head())
    else:
        print("DEBUG: df es None")

    # Fallback: si no hay datos, usar ejemplo
    if df is None or df.empty or len(df) < 2:
        print("DataFrame vacío o insuficiente. Usando datos de ejemplo para generar gráficos.")
        df = pd.DataFrame({
            "rating": [7.5, 8.2, 6.9, 7.8, 9.0],
            "genre": [["Action","Drama"], ["Comedy"], ["Drama"], ["Action","Thriller"], ["Comedy","Romance"]]
        })

    sns.set_style("whitegrid")

    # ------------------------------
    # Gráfico 1: Distribución de Ratings
    # ------------------------------
    plt.figure(figsize=(10, 6))
    sns.histplot(df['rating'], bins=10, kde=True, color='#e74c3c')
    plt.title('Distribución de Calificaciones (IMDb Rating)', fontsize=16)
    plt.xlabel('Rating', fontsize=12)
    plt.ylabel('Frecuencia', fontsize=12)

    plt.savefig(os.path.join(OUTPUT_DIR, 'rating_distribution.png'))
    plt.close()
    print("Gráfico 1 guardado: rating_distribution.png")

    # ------------------------------
    # Gráfico 2: Conteo de Películas por Género
    # ------------------------------
    plt.figure(figsize=(12, 7))
    # Desanidar géneros
    all_genres = df['genre'].explode().str.strip()
    genre_counts = all_genres.value_counts().head(8)

    sns.barplot(x=genre_counts.index, y=genre_counts.values, palette='viridis')
    plt.title('Top 8 Géneros por Conteo de Películas', fontsize=16)
    plt.xlabel('Género', fontsize=12)
    plt.ylabel('Número de Películas', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    plt.savefig(os.path.join(OUTPUT_DIR, 'genre_count.png'))
    plt.close()
    print("Gráfico 2 guardado: genre_count.png")

if __name__ == "__main__":
    generate_visualizations()
