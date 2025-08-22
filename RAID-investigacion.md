# Investigación sobre RAID
**Tarea #996** - Entrega: 22/08/2025

## ¿Qué es RAID?
RAID (Redundant Array of Independent Disks) es una tecnología que combina múltiples discos duros físicos en una única unidad lógica para mejorar el rendimiento, la capacidad y/o la fiabilidad de los datos.

## Niveles de RAID más comunes

### RAID 0 (Striping)
- **Descripción**: Divide los datos en bloques y los distribuye entre dos o más discos
- **Ventajas**: Máximo rendimiento y capacidad
- **Desventajas**: Sin redundancia - si un disco falla, se pierden todos los datos
- **Mínimo de discos**: 2
- **Capacidad útil**: 100%

### RAID 1 (Mirroring)
- **Descripción**: Duplica los datos exactamente en dos o más discos
- **Ventajas**: Alta redundancia y confiabilidad
- **Desventajas**: Capacidad reducida (50% con 2 discos)
- **Mínimo de discos**: 2
- **Capacidad útil**: 50%

### RAID 5 (Striping con paridad distribuida)
- **Descripción**: Combina striping con paridad distribuida entre todos los discos
- **Ventajas**: Balance entre rendimiento, capacidad y redundancia
- **Desventajas**: Rendimiento de escritura más lento debido al cálculo de paridad
- **Mínimo de discos**: 3
- **Capacidad útil**: (n-1)/n (ej: 67% con 3 discos)

### RAID 6 (Striping con doble paridad)
- **Descripción**: Similar a RAID 5 pero con doble paridad
- **Ventajas**: Tolera el fallo de dos discos simultáneamente
- **Desventajas**: Mayor overhead de capacidad, menor rendimiento de escritura
- **Mínimo de discos**: 4
- **Capacidad útil**: (n-2)/n (ej: 50% con 4 discos)

### RAID 10 (1+0)
- **Descripción**: Combina mirroring y striping (primero espeja, luego divide)
- **Ventajas**: Alto rendimiento y alta redundancia
- **Desventajas**: Mayor costo por capacidad útil
- **Mínimo de discos**: 4
- **Capacidad útil**: 50%

## Implementaciones de RAID

### Hardware RAID
- Usa controlador dedicado
- Mejor rendimiento
- Independiente del sistema operativo
- Más costoso

### Software RAID
- Implementado por el sistema operativo
- Más económico
- Dependiente del rendimiento del CPU
- Más flexible

## Casos de uso

- **RAID 0**: Edición de video, caching (donde la redundancia no es crítica)
- **RAID 1**: Sistemas críticos, servidores pequeños
- **RAID 5**: Servidores de archivos, almacenamiento general
- **RAID 6**: Almacenamiento de backups, archivos importantes
- **RAID 10**: Bases de datos, servidores de alto rendimiento

