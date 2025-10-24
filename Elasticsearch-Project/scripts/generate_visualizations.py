#!/usr/bin/env python3
"""
Script que genera visualizaciones REALES del dataset de películas
"""

import json
import matplotlib.pyplot as plt
import pandas as pd
import os

def load_movies_data():
    """Cargar datos de películas"""
    with open('data/movies.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def create_visualizations():
    """Crear visualizaciones y guardarlas como imágenes"""
    movies = load_movies_data()
    df = pd.DataFrame(movies)
    
    # Configurar el estilo de las gráficas
    plt.style.use('default')
    
    # Crear figura con 4 subplots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Análisis de Dataset de Películas - Elasticsearch Project', fontsize=16, fontweight='bold')
    
    # 1. Gráfica de películas por año
    year_counts = df['year'].value_counts().sort_index()
    bars = ax1.bar(year_counts.index, year_counts.values, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'])
    ax1.set_title('Películas por Año', fontsize=14, fontweight='bold')
    ax1.set_xlabel('Año')
    ax1.set_ylabel('Número de Películas')
    # Agregar valores en las barras
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}', ha='center', va='bottom')
    
    # 2. Distribución de ratings
    ax2.hist(df['rating'], bins=6, color='#FFA07A', alpha=0.7, edgecolor='black')
    ax2.set_title('Distribución de Ratings', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Rating')
    ax2.set_ylabel('Frecuencia')
    ax2.grid(True, alpha=0.3)
    
    # 3. Duración vs Rating
    scatter = ax3.scatter(df['duration'], df['rating'], c=df['rating'], 
                         cmap='viridis', s=100, alpha=0.6)
    ax3.set_title('Duración vs Rating', fontsize=14, fontweight='bold')
    ax3.set_xlabel('Duración (minutos)')
    ax3.set_ylabel('Rating')
    ax3.grid(True, alpha=0.3)
    # Agregar colorbar
    plt.colorbar(scatter, ax=ax3)
    
    # 4. Géneros más comunes
    all_genres = [genre for genres in df['genre'] for genre in genres]
    genre_counts = pd.Series(all_genres).value_counts().head(6)
    bars_genres = ax4.barh(genre_counts.index, genre_counts.values, color='#20B2AA')
    ax4.set_title('Géneros Más Comunes', fontsize=14, fontweight='bold')
    ax4.set_xlabel('Número de Películas')
    # Agregar valores en las barras
    for bar in bars_genres:
        width = bar.get_width()
        ax4.text(width + 0.1, bar.get_y() + bar.get_height()/2.,
                f'{int(width)}', ha='left', va='center')
    
    plt.tight_layout()
    
    # Guardar la gráfica
    os.makedirs('docs/assets', exist_ok=True)
    plt.savefig('docs/assets/movies_visualization.png', dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.close()
    
    print("✅ Visualizaciones generadas exitosamente!")
    return df

def main():
    """Función principal"""
    print("🎬 Generando visualizaciones para el dataset de películas...")
    df = create_visualizations()
    print(f"📊 Procesadas {len(df)} películas")
    print("🖼️  Gráficas guardadas en: docs/assets/movies_visualization.png")

if __name__ == "__main__":
    main()
