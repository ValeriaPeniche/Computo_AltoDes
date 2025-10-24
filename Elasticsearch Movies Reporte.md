# Reporte de Tarea: Visualización de Datos de Películas con Elasticsearch y GitHub Pages
**Tarea:** #989 - Entrega: 24/10/2025

## Información General
- **Objetivo de la Tarea:** Usar Elasticsearch para cargar un dataset de películas y generar visualizaciones en GitHub Pages automáticamente mediante GitHub Actions y Python.
- **Tecnologías utilizadas:** Python, Pandas, Matplotlib, Seaborn, Elasticsearch Cloud, GitHub Actions, GitHub Pages.

## Dataset
Se utilizó un dataset de ejemplo de películas con las siguientes columnas principales:  
- `title`: nombre de la película  
- `rating`: calificación IMDb  
- `genre`: lista de generos

## Flujo de Trabajo Automatizado (GitHub Actions)
1. Cada push al branch `main` dispara el workflow definido en `.github/workflows/deploy.yml`.
2. Pasos principales:
   - Instalación de dependencias (`elasticsearch`, `pandas`, `matplotlib`, `seaborn`).
   - Carga de datos a Elasticsearch (o fallback a datos de ejemplo).
   - Generación de gráficos PNG en `docs/assets`.
   - Preparación de GitHub Pages (`docs` como source, deshabilitado Jekyll).
   - Subida de artifacts y despliegue automático en GitHub Pages.
3. El workflow genera los gráficos:
   - Distribución de Ratings (IMDb)
   - Conteo de Películas por Género
4. Los gráficos deberían estar en: `docs/assets/rating_distribution.png` y `docs/assets/genre_count.png`.

## Resultados
- La página de GitHub Pages se generó correctamente en:  
  [https://valeriapeniche.github.io/Computo_AltoDes/](https://valeriapeniche.github.io/Computo_AltoDes/)

## Conclusiones
- La automatización con GitHub Actions permite que cada push a `main` genere y despliegue la página automáticamente.
- Aunque aún no se generaron las imágenes de los gráficos reales, se verificó que el flujo de GitHub Pages funciona correctamente.
- Este ejercicio refuerza la comprensión de la integración de Python, Elasticsearch y GitHub Pages para visualización de datos en tiempo real.

