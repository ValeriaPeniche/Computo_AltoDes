# Lab 3.1: Working with Amazon S3
**Curso:** AWS Academy Cloud Developing
**Fecha de realización:** 15 de octubre de 2025

## Contexto del Proyecto
Continuando con el desarrollo de la presencia en línea de la cafetería, en este laboratorio se implementó un sitio web estático seguro utilizando Amazon S3, aplicando políticas de seguridad basadas en direcciones IP para restringir el acceso durante la fase de desarrollo.

## Objetivos del Laboratorio
- Crear y configurar un bucket de S3 para hosting de sitio web estático
- Aplicar políticas de bucket para restringir acceso por dirección IP
- Cargar objetos del sitio web utilizando AWS CLI
- Verificar la funcionalidad del sitio web y las restricciones de seguridad
- Preparar la base para futuras integraciones con servicios dinámicos

## Actividades Realizadas

### Tarea 1: Configuración del Entorno IDE
1. **Instalación de Boto3**
   - Se ejecutó `sudo pip3 install boto3` para asegurar compatibilidad con scripts Python
   - Se verificó la instalación correcta del SDK

2. **Descarga de Recursos**
   - Se descargó y extrajo el archivo `code.zip` con recursos del laboratorio
   - Los archivos se ubicaron en `/home/ec2-user/environment`

3. **Verificación de AWS CLI**
   - Se confirmó que AWS CLI versión 2 estaba operativa

### Tarea 2: Creación del Bucket S3
1. **Creación mediante AWS CLI**
   - Se utilizó: `aws s3api create-bucket --bucket <bucket-name> --region us-east-1`
   - El nombre del bucket incluyó iniciales, fecha y palabra clave para unicidad

2. **Configuración de Seguridad**
   - Se mantuvo activa la configuración "Bloquear todo el acceso público"
   - Se ajustaron permisos para permitir políticas personalizadas
   - Se mantuvieron protecciones básicas de seguridad

### Tarea 3: Implementación de Política de Seguridad
1. **Creación de Política JSON**
   - Se desarrolló `website_security_policy.json` con dos declaraciones:
     - **Declaración 1**: Permite acceso `s3:GetObject` solo desde IP específica
     - **Declaración 2**: Restringe acceso a `report.html` sin URL prefirmada

2. **Aplicación con Python/Boto3**
   - Se editó el script `permissions.py` con el nombre del bucket
   - Se ejecutó `python3 permissions.py` para aplicar la política
   - La política se adjuntó exitosamente al bucket

### Tarea 4 y 5: Carga y Prueba del Sitio Web
1. **Carga de Archivos**
   - Se utilizó: `aws s3 cp ../resources/website s3://<bucket-name>/ --recursive --cache-control "max-age=0"`
   - Se desactivó cache del navegador para desarrollo activo

2. **Pruebas de Acceso**
   - **Acceso Exitoso**: Desde IP autorizada, el sitio cargó correctamente
   - **Acceso Denegado**: Desde IP externa, se recibió error `AccessDenied`
   - Se confirmó efectividad de las restricciones de seguridad

### Tarea 6: Análisis de Arquitectura del Sitio
1. **Estructura de Archivos**
   - `index.html`: Página principal con referencias a CSS y JavaScript
   - `config.js`: Variables para futuras integraciones (API Gateway, Cognito)
   - `pastries.js`: Lógica para cargar productos desde JSON estático
   - `all_products.json`: Datos de productos en formato JSON

2. **Preparación para Escalabilidad**
   - Arquitectura diseñada para migrar a servicios dinámicos
   - Variables de configuración listas para futuras integraciones

## Resultados Obtenidos
- Bucket de S3 creado exitosamente con nombre único
- Política de seguridad aplicada correctamente restringiendo por IP
- Sitio web estático cargado y accesible desde red autorizada
- Restricciones de seguridad validadas con pruebas de acceso
- Base arquitectónica establecida para futuras integraciones
- Configuración de cache optimizada para desarrollo

## Conclusiones
Se estableció exitosamente una base web segura para la cafetería utilizando Amazon S3. La implementación de políticas de seguridad basadas en IP garantiza que el sitio sea accesible solo durante el desarrollo por el equipo autorizado. La arquitectura preparada permite una transición fluida hacia servicios dinámicos en laboratorios futuros, estableciendo las bases para un sitio web escalable y seguro.
