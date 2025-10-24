#!/usr/bin/env python3
"""
Script para generar el reporte HTML con las visualizaciones
"""

import json
import os

def create_html_report():
    """Crear el archivo HTML final con las visualizaciones"""
    
    html_content = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tarea #989 - Elasticsearch con Visualizaciones</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: white;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
            border-radius: 10px;
            margin-top: 20px;
            margin-bottom: 20px;
        }
        header {
            text-align: center;
            padding: 40px 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 10px;
            margin-bottom: 30px;
        }
        header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }
        .stat-card {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            border-left: 4px solid #667eea;
        }
        .stat-card h3 {
            font-size: 2em;
            color: #667eea;
            margin-bottom: 10px;
        }
        .visualization {
            text-align: center;
            margin: 40px 0;
        }
        .chart-image {
            max-width: 100%;
            height: auto;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            border: 1px solid #ddd;
        }
        .tech-stack {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
        }
        footer {
            text-align: center;
            padding: 20px;
            margin-top: 40px;
            border-top: 1px solid #ddd;
            color: #666;
        }
        @media (max-width: 768px) {
            .container {
                margin: 10px;
                padding: 15px;
            }
            header h1 {
                font-size: 2em;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🎬 Tarea #989 Co1>
            <h2>Elasticsearch con Visualizaciones - GitHub Pages</h2>
            <p>Dataset analizado y visualizado automáticamente con GitHub Actions</p>
        </header>

        <section class="stats-grid">
            <div class="stat-card">
                <h3>8</h3>
                <p>Películas Analizadas</p>
            </div>
            <div class="stat-card">
                <h3>1990-2010</h3>
                <p>Rango de Años</p>
            </div>
            <div class="stat-card">
                <h3>8.8</h3>
                <p>Rating Promedio</p>
            </div>
            <div class="stat-card">
                <h3>6</h3>
                <p>Géneros Diferentes</p>
            </div>
        </section>

        <section class="visualization">
            <h2>📊 Visualizaciones Generadas Automáticamente</h2>
            <p>Estas gráficas se generan con Python, Pandas y Matplotlib en cada actualización</p>
            <img src="assets/movies_visualization.png" alt="Visualizaciones de análisis de películas" class="chart-image">
        </section>

        <section class="tech-stack">
            <h2>🛠️ Tecnologías Utilizadas</h2>
            <div class="stats-grid">
                <div class="stat-card">
                    <h3>Python</h3>
                    <p>Procesamiento y visualización</p>
                </div>
                <div class="stat-card">
                    <h3>Pandas</h3>
                    <p>Análisis de datos</p>
                </div>
                <div class="stat-card">
                    <h3>Matplotlib</h3>
                    <p>Generación de gráficas</p>
                </div>
                <div class="stat-card">
                    <h3>GitHub Actions</h3>
                    <p>Automatización CI/CD</p>
                </div>
            </div>
        </section>

        <footer>
            <p><strong>Tarea #989</strong> - Elasticsearch con GitHub Pages</p>
            <p><strong>Fecha:</strong> Octubre 2025</p>
        </footer>
    </div>
</body>
</html>
'''
    
    # Escribir el archivo HTML
    with open('docs/index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("✅ Reporte HTML generado exitosamente!")

if __name__ == "__main__":
    create_html_report()
