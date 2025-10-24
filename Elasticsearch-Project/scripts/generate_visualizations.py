#!/usr/bin/env python3
import json
import matplotlib.pyplot as plt
import pandas as pd
import os

def load_movies_data():
    with open('Elasticsearch-Project/data/movies.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def create_visualizations():
    movies = load_movies_data()
    df = pd.DataFrame(movies)
    
    # Crear gráficas simples pero funcionales
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))
    
    # 1. Películas por año
    year_counts = df['year'].value_counts().sort_index()
    ax1.bar(year_counts.index, year_counts.values, color='skyblue')
    ax1.set_title('Películas por Año')
    
    # 2. Distribución de ratings
    ax2.hist(df['rating'], bins=6, color='lightgreen', alpha=0.7)
    ax2.set_title('Distribución de Ratings')
    
    # 3. Duración vs Rating
    ax3.scatter(df['duration'], df['rating'], color='coral', s=60)
    ax3.set_title('Duración vs Rating')
    ax3.set_xlabel('Duración (min)')
    ax3.set_ylabel('Rating')
    
    # 4. Géneros
    all_genres = [genre for genres in df['genre'] for genre in genres]
    genre_counts = pd.Series(all_genres).value_counts().head(5)
    ax4.barh(genre_counts.index, genre_counts.values, color='gold')
    ax4.set_title('Géneros Más Comunes')
    
    plt.tight_layout()
    os.makedirs('Elasticsearch-Project/docs/assets', exist_ok=True)
    plt.savefig('Elasticsearch-Project/docs/assets/movies_visualization.png', 
                dpi=150, bbox_inches='tight')
    plt.close()
    
    print("✅ Gráficas generadas!")
    return df

if __name__ == "__main__":
    create_visualizations()
