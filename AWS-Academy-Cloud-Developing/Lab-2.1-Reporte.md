# Lab 2.1: Exploring AWS CloudShell and an IDE
**Curso:** AWS Academy Cloud Developing
**Fecha de realización:** 15 de octubre de 2025

## Contexto del Proyecto
Como parte del rol de Sofía, desarrolladora asignada para crear la presencia en línea de una pequeña cafetería, se exploraron diferentes entornos de desarrollo en AWS para determinar la herramienta más adecuada para el proyecto.

## Objetivos del Laboratorio
- Explorar AWS CloudShell y sus funcionalidades
- Familiarizarse con el IDE de Visual Studio Code provisto por AWS
- Determinar el entorno de desarrollo más adecuado para el proyecto de la cafetería
- Ejecutar comandos AWS CLI y código AWS SDK (Boto3) en ambos entornos
- Copiar archivos entre Amazon S3, CloudShell y el IDE

## Actividades Realizadas

### Tarea 1: Explorar AWS CloudShell
1. **Acceso y verificación de AWS CLI**
   - Se accedió a CloudShell desde la Consola de AWS
   - Se verificó la versión de AWS CLI (`aws --version`)
   - Se confirmó la versión 2.x.x instalada

2. **Ejecución de comandos AWS CLI**
   - Se ejecutó `aws s3 ls` para listar buckets existentes
   - Se demostró la funcionalidad de terminal múltiple

3. **Ejecución de código Python con Boto3**
   - Se cargó y ejecutó el archivo `list-buckets.py`
   - Se verificó la interacción con servicios AWS mediante SDK

4. **Copia de archivos a S3**
   - Se copió `list-buckets.py` al bucket de S3 usando `aws s3 cp`

### Tarea 2: Explorar el IDE de VS Code
1. **Interfaz y exploración**
   - Se exploró el editor principal y panel de navegación
   - Se identificó el terminal Bash integrado

2. **Copia de archivos desde S3**
   - Se descargó `list-buckets.py` desde S3 al IDE local

3. **Instalación de Boto3**
   - Se instaló el SDK con `sudo pip3 install boto3`
   - Se resolvió error `ModuleNotFoundError: No module named 'boto3'`

4. **Creación y carga de archivo web**
   - Se creó `index.html` con contenido básico
   - Se cargó al bucket de S3 para posible hosting web

## Resultados Obtenidos
- Conexión exitosa a AWS CloudShell y ejecución de comandos CLI
- Ejecución correcta de scripts Python con Boto3 en CloudShell
- Exploración completa del IDE de VS Code con todas sus funcionalidades
- Instalación exitosa del AWS SDK para Python (Boto3)
- Transferencia de archivos entre S3, CloudShell y el IDE
- Creación y despliegue de archivo HTML básico

## Conclusiones
AWS CloudShell demostró ser una herramienta eficiente para ejecución rápida de comandos y scripts, ideal para tareas administrativas. Sin embargo, para el desarrollo del sitio web de la cafetería, el IDE de VS Code ofrece ventajas significativas con su editor gráfico, explorador de archivos visual y capacidades de depuración integradas. La combinación de ambas herramientas proporciona un ecosistema completo para el desarrollo en la nube de AWS.
