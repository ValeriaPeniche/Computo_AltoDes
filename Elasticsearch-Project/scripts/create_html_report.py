#!/usr/bin/env python3
html_content = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Tarea #989 - Visualizaciones</title>
    <style>
        body { font-family: Arial; max-width: 1000px; margin: auto; padding: 20px; }
        header { text-align: center; background: #f0f0f0; padding: 20px; border-radius: 10px; }
        img { max-width: 100%; border: 1px solid #ddd; border-radius: 5px; margin: 20px 0; }
        footer { text-align: center; margin-top: 30px; color: #666; }
    </style>
</head>
<body>
    <header>
        <h1>Tarea Completada</h1>
        <p>Visualizaciones generadas con GitHub Actions</p>
    </header>
    
    <section>
        <h2>Análisis de Dataset de Películas</h2>
        <img src="assets/movies_visualization.png" alt="Gráficas de análisis">
    </section>
    
    <section>
        <h3>Métricas del Dataset</h3>
        <ul>
            <li><strong>8 películas</strong> analizadas</li>
            <li><strong>Rating promedio:</strong> 8.8/10</li>
            <li><strong>Rango de años:</strong> 1972-2010</li>
            <li><strong>6 géneros</strong> diferentes</li>
        </ul>
    </section>
    
    <footer>
        <p><strong>Tarea #989</strong> - Elasticsearch con GitHub Pages</p>
    </footer>
</body>
</html>
'''
with open('Elasticsearch-Project/docs/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
print("✅ HTML generado!")
