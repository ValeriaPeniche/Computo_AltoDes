# Lab 6.1: Developing REST APIs with Amazon API Gateway
**Curso:** AWS Academy Cloud Developing
**Fecha de realización:** 19 de octubre de 2025

## Contexto del Proyecto
Para conectar el frontend estático de la cafetería con los datos dinámicos almacenados en DynamoDB, en este laboratorio se implementó una API REST utilizando Amazon API Gateway, estableciendo los endpoints necesarios para la aplicación web con respuestas simuladas como preparación para la integración completa.

## Objetivos del Laboratorio
- Crear una API REST utilizando Amazon API Gateway
- Definir endpoints con integraciones MOCK para desarrollo
- Implementar configuración CORS para endpoints GET
- Desplegar la API a una etapa de producción
- Actualizar el frontend para consumir la API Gateway
- Preparar la arquitectura para integración con Lambda y DynamoDB

## Actividades Realizadas

### Tarea 1: Preparación del Entorno
1. **Configuración Inicial**
   - Se descargó y extrajo `code.zip` con recursos actualizados
   - Se ejecutó `resources/setup.sh` para instalar dependencias
   - Se cargó nueva versión del sitio web al bucket S3

2. **Verificación del Estado Actual**
   - Se confirmó que el sitio web utilizaba datos estáticos de archivos JSON
   - Se identificó la necesidad de migrar a fuentes de datos dinámicas

### Tarea 2 y 3: Endpoints GET (/products y /products/on_offer)
1. **Creación de la API Principal**
   - Se ejecutó `create_products_api.py` para crear `ProductsApi`
   - Se definió recurso `/products` con método GET

2. **Configuración de Integraciones MOCK**
   - **Endpoint `/products`**: Respuesta simulada con estructura de datos DynamoDB
   - **Endpoint `/products/on_offer`**: Respuesta con producto único en oferta
   - Ambos endpoints incluyeron contenedores de tipos de datos DynamoDB ("S", "N")

3. **Implementación de CORS**
   - Se configuraron encabezados `Access-Control-Allow-Origin`
   - Se habilitó acceso cross-origin para el sitio web estático en S3
   - Se validó funcionalidad mediante pruebas en consola API Gateway

### Tarea 4: Endpoint POST (/create_report)
1. **Creación del Endpoint**
   - Se ejecutó `create_report_api.py` para recurso `/create_report`
   - Se definió método POST con integración MOCK

2. **Respuesta Simulada**
   - Mensaje: `{"msg_str": "report requested, check your phone shortly"}`
   - Preparación para futura implementación con autenticación
   - Configuración diferenciada de CORS para endpoints autenticados

### Tarea 5 y 6: Implementación y Actualización del Frontend
1. **Despliegue de la API**
   - Se implementó `ProductsApi` a etapa `prod`
   - Se obtuvo URL de invocación: `https://<api-id>.execute-api.us-east-1.amazonaws.com/prod`

2. **Actualización de Configuración**
   - Se editó `resources/website/config.js`
   - Se reemplazó valor `null` en `API_GW_BASE_URL_STR` con URL de la API
   - Se ejecutó `update_config.py` para cargar cambios a S3

3. **Validación Final**
   - Vista "on offer" mostró producto único (respuesta de endpoint MOCK)
   - Vista "view all" mostró tres productos (respuesta de endpoint MOCK)
   - Consola del navegador confirmó consumo de API Gateway
   - Se verificó transición exitosa de datos estáticos a dinámicos

## Resultados Obtenidos
- API REST `ProductsApi` creada y desplegada exitosamente
- Tres endpoints configurados: 2 GET con CORS, 1 POST para autenticación futura
- Integraciones MOCK funcionando correctamente
- Frontend actualizado para consumir API Gateway
- Configuración CORS implementada para acceso cross-origin
- Arquitectura preparada para integración con servicios backend

## Endpoints Implementados
```http
GET    /products          - Obtener todos los productos
GET    /products/on_offer - Obtener productos en oferta
POST   /create_report     - Solicitar informe (futura autenticación)
 ```
## Conclusiones
La implementación exitosa de la API REST con API Gateway marca un hito crucial en la arquitectura serverless de la cafetería. La transición del frontend para consumir endpoints MOCK demuestra la preparación para la integración completa con DynamoDB mediante funciones Lambda. La configuración de CORS garantiza la comunicación segura entre el sitio web estático y los servicios backend, estableciendo las bases para una aplicación web completamente dinámica y escalable.
