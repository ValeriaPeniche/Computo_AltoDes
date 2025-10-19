# Lab 5.1: Working with DynamoDB
**Curso:** AWS Academy Cloud Developing
**Fecha de realización:** 19 de octubre de 2025

## Contexto del Proyecto
Para escalar la plataforma web de la cafetería, en este laboratorio se migró la información del menú desde archivos JSON estáticos a Amazon DynamoDB, una base de datos NoSQL altamente escalable, permitiendo gestionar dinámicamente productos, precios y ofertas especiales.

## Objetivos del Laboratorio
- Crear y definir una tabla DynamoDB para almacenar productos alimenticios
- Gestionar elementos utilizando AWS CLI y SDK para Python (Boto3)
- Implementar expresiones condicionales para prevenir sobrescrituras accidentales
- Utilizar procesamiento por lotes para carga eficiente de datos
- Consultar datos mediante operaciones scan y query
- Crear índices secundarios globales (GSI) para consultas optimizadas

## Actividades Realizadas

### Tarea 1: Preparación del Entorno
1. **Descarga de Recursos**
   - Se descargó y extrajo `code.zip` con scripts Python y archivos JSON
   - Se organizaron los recursos en el directorio de trabajo

2. **Actualización de AWS CLI**
   - Se ejecutó `./resources/setup.sh` para establecer permisos
   - Se verificó la compatibilidad con operaciones DynamoDB

### Tarea 2: Creación de Tabla DynamoDB
1. **Definición de la Tabla**
   - Se editó `create_table.py` para crear tabla `FoodProducts`
   - Se estableció `product_name` como clave primaria (Hash Key)
   - Se configuró tipo de atributo como String ('S')

2. **Verificación**
   - Se ejecutó `python3 create_table.py`
   - Se confirmó en consola AWS que la tabla estaba en estado "Activo"

### Tarea 3 y 4: Gestión de Datos con Expresiones Condicionales
1. **Comportamiento Default de Put-Item**
   - Se insertaron productos `best cake` y `best pie` via CLI
   - Se confirmó que `put-item` sobrescribe registros existentes
   - Se identificó riesgo de pérdida de atributos en actualizaciones

2. **Implementación de Expresiones Condicionales**
   - Se utilizó `attribute_not_exists(product_name)` para prevenir duplicados
   - Se validó que re-inserciones fallan con `ConditionalCheckFailedException`
   - Se implementó lógica en `conditional_put.py` para inserciones seguras

### Tarea 5: Carga por Lotes de Datos
1. **Carga con Sobrescritura**
   - Se ejecutó `test_batch_put.py` con `overwrite_by_pkeys=['product_name']`
   - Se observó que duplicados causaban sobrescritura (último registro prevalece)

2. **Carga sin Sobrescritura**
   - Se modificó script eliminando `overwrite_by_pkeys`
   - Se validó comportamiento de "falla rápida" con duplicados
   - Se identificó como preferible para producción

3. **Carga de Datos de Producción**
   - Se utilizó `batch_put.py` para cargar 26+ items del menú real
   - Se procesó exitosamente archivo `all_products.json`

### Tarea 6 y 7: Consultas e Índices Secundarios
1. **Operación Scan**
   - Se implementó `get_all_items.py` usando `scan()`
   - Se recuperaron todos los registros para menú completo

2. **Operación GetItem**
   - Se utilizó `get_one_item.py` con `get_item()`
   - Se consultaron elementos individuales por clave primaria

3. **Índice Secundario Global (GSI)**
   - Se creó GSI `special_GSI` con clave HASH en atributo `special`
   - Se ejecutó `add_gsi.py` y se monitoreó estado "Activo"
   - Se implementó consulta filtrada excluyendo productos "out of stock"

## Resultados Obtenidos
- Tabla DynamoDB `FoodProducts` creada exitosamente
- Mecanismos de prevención de duplicados implementados
- Carga por lotes de 26+ productos del menú completada
- Índice secundario `special_GSI` configurado y operativo
- Consultas optimizadas para menú completo y ofertas especiales
- Arquitectura preparada para integración con API

## Conclusiones
La migración exitosa a DynamoDB transformó la gestión del menú de estática a dinámica, permitiendo actualizaciones en tiempo real y consultas optimizadas. La implementación de índices secundarios facilita la exhibición de ofertas especiales, mientras que las expresiones condicionales garantizan la integridad de los datos. Esta base establece las condiciones para integrar una API REST que permita al sitio web consumir datos dinámicos del menú.
