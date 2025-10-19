# Lab 7.1: Creating Lambda Functions Using the AWS SDK for Python
**Curso:** AWS Academy Cloud Developing
**Fecha de realización:** 19 de octubre de 2025

## Contexto del Proyecto
Para completar la arquitectura serverless de la cafetería, en este laboratorio se reemplazaron las integraciones MOCK de API Gateway con funciones AWS Lambda, estableciendo una conexión dinámica y en tiempo real con la base de datos DynamoDB, culminando en una aplicación web completamente funcional.

## Objetivos del Laboratorio
- Crear funciones Lambda utilizando AWS SDK para Python (Boto3)
- Configurar permisos IAM para acceso seguro a DynamoDB
- Reemplazar integraciones MOCK con invocaciones Lambda en API Gateway
- Resolver problemas de CORS en la transición a Lambda
- Implementar lógica de negocio para consultas dinámicas
- Validar el flujo completo de datos desde frontend hasta base de datos

## Actividades Realizadas

### Tarea 1: Configuración del Entorno
1. **Recreación de Recursos**
   - Se ejecutó script de configuración para recrear recursos previos
   - Se verificó estado de tabla `FoodProducts` con índice `special_GSI`
   - Se confirmó funcionalidad de `ProductsApi` con endpoints MOCK

2. **Estado Inicial del Frontend**
   - Sitio web consumiendo respuestas MOCK mínimas
   - Solo un elemento visible en sección "Browse Pastries"
   - Preparación para transición a datos dinámicos

### Tarea 2: Función Lambda get_all_products
1. **Desarrollo de Lógica de Negocio**
   - Se editó `get_all_products_code.py` con dos modos de operación:
     - **Scan completo**: Sin variable de ruta, devuelve todos los productos
     - **Scan filtrado**: Con `offer_path_str`, consulta GSI `special_GSI`
   - Se implementó filtro para excluir productos "out of stock"

2. **Configuración de Seguridad**
   - Se utilizó rol IAM `LambdaAccessToDynamoDB` con permisos de solo lectura
   - Se empaquetó código en archivo ZIP y se subió a bucket S3
   - Se creó función Lambda mediante `get_all_products_wrapper.py`

3. **Pruebas de Validación**
   - **Evento Products**: Retornó todos los elementos de DynamoDB
   - **Evento onOffer**: Retornó solo productos en oferta especial

### Tarea 3: Integración API Gateway con Lambda
1. **Actualización de Endpoints GET**
   - Se reemplazó integración MOCK por invocación Lambda en `/products`
   - Se configuró mapeo de parámetros para `/products/on_offer`:
     ```json
     { "path": "$context.resourcePath" }
     ```

2. **Resolución de Problemas CORS**
   - Se perdió configuración CORS al cambiar integración
   - Se restauró mediante opción "Habilitar CORS" en consola API Gateway
   - Se estableció `Access-Control-Allow-Origin: *`

3. **Despliegue de Cambios**
   - Se implementó API a etapa `prod` para aplicar actualizaciones
   - Se validó funcionalidad de ambos endpoints GET

### Tarea 4 y 5: Función create_report
1. **Desarrollo de Función de Reportes**
   - Se creó `create_report` con código en `create_report_code.py`
   - Se implementó mensaje estático: `"Report processing..."`
   - Función preparada para futura expansión con lógica compleja

2. **Configuración de Endpoint POST**
   - Se actualizó `/create_report` para invocar función Lambda
   - Se validó respuesta con "R" mayúscula como marcador
   - Se implementó cambios en etapa `prod`

### Tarea 6: Validación Final del Sistema
1. **Pruebas de Integración**
   - **Vista "on offer"**: Mostró 6 productos especiales disponibles
   - **Vista "view all"**: Mostró 26 productos completos del menú
   - **CORS**: Comunicación cross-origin funcionando correctamente

2. **Prueba en Tiempo Real**
   - Se modificó precio de producto en DynamoDB
   - Cambio se reflejó instantáneamente en el sitio web
   - Se confirmó flujo de datos en tiempo real

3. **Verificación de Arquitectura Completa**
   - S3 (Frontend) → API Gateway → Lambda → DynamoDB (Backend)
   - Todas las componentes serverless operando correctamente

## Resultados Obtenidos
- Dos funciones Lambda creadas: `get_all_products` y `create_report`
- Integración completa entre API Gateway y Lambda
- Problemas de CORS resueltos exitosamente
- Permisos IAM configurados para acceso seguro a DynamoDB
- Sitio web consumiendo datos dinámicos en tiempo real
- Arquitectura serverless completamente funcional
- Capacidad de actualizaciones instantáneas del menú

## Conclusiones
La implementación exitosa de funciones Lambda marca la culminación de la arquitectura serverless para la cafetería. El sistema ahora opera con un flujo completo de datos en tiempo real, desde la interfaz web hasta la base de datos, demostrando escalabilidad, eficiencia en costos y mantenibilidad. La resolución de problemas de CORS garantiza una experiencia de usuario seamless, mientras que la estructura modular prepara el terreno para futuras expansiones, incluyendo la integración de autenticación con Amazon Cognito.
