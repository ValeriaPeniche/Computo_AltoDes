#!/usr/bin/env python3
"""
Script para generar visualizaciones (gráficos) con Matplotlib y guardarlas para GitHub Pages.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
import query_elasticsearch # Importamos el script de consulta

# La ruta de salida debe ser relativa a la ubicación del script (scripts/)
OUTPUT_DIR = '../docs/assets' 
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_visualizations():
    """Consulta datos de ES/Local y genera gráficos PNG."""
    print("🎨 Generando visualizaciones...")
    
    # Obtener datos usando el script de consulta
    df = query_elasticsearch.get_elasticsearch_data()
    
    if df.empty or len(df) < 2:
        print("⚠️ DataFrame vacío o insuficiente para graficar. Deteniendo.")
        return

    # ----------------------------------------------------
    # Gráfico 1: Distribución de Ratings
    # ----------------------------------------------------
    plt.figure(figsize=(10, 6))
    sns.histplot(df['rating'], bins=len(df), kde=True, color='#3498db')
    plt.title('Distribución de Calificaciones (IMDb Rating)', fontsize=16)
    plt.xlabel('Rating', fontsize=12)
    plt.ylabel('Frecuencia', fontsize=12)
    
    # Guardar en la carpeta docs/assets
    plt.savefig(os.path.join(OUTPUT_DIR, 'rating_distribution.png'))
    plt.close()
    print("✅ Gráfico 1 guardado: rating_distribution.png")
    
    # ----------------------------------------------------
    # Gráfico 2: Conteo de Películas por Género
    # ----------------------------------------------------
    plt.figure(figsize=(12, 7))
    
    # Desanidar los géneros para contar correctamente (ya que 'genre' es una lista)
    all_genres = df['genre'].explode().str.strip() 
    genre_counts = all_genres.value_counts().head(8)
    
    sns.barplot(x=genre_counts.index, y=genre_counts.values, palette='plasma')
    plt.title('Top Géneros por Conteo de Películas', fontsize=16)
    plt.xlabel('Género', fontsize=12)
    plt.ylabel('Número de Películas', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout() # Ajusta el layout para que las etiquetas no se corten
    
    # Guardar en la carpeta docs/assets
    plt.savefig(os.path.join(OUTPUT_DIR, 'genre_count.png'))
    plt.close()
    print("✅ Gráfico 2 guardado: genre_count.png")


if __name__ == "__main__":
    # Necesitas instalar las librerías: pip install elasticsearch pandas matplotlib seaborn
    generate_visualizations()
