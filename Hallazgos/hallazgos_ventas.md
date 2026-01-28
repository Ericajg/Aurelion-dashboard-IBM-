# Inspección inicial — Dataset Ventas

Fecha: 28 de octubre de 2025  
Archivo analizado: ventas.xlsx  
Notebook fuente: limpieza_ventas.ipynb

## Objetivo
Realizar la inspección inicial del dataset de ventas para identificar problemas de calidad y estructura antes de la limpieza.

## Pasos realizados
1. Carga de datos  
   - Código: `pd.read_excel(r"...\ventas.xlsx")`  
   - Vista previa: `df_ventas.head(10)`

2. Inspección general  
   - `df_ventas.info()` — tipos de datos, nulos y uso de memoria.  
   - `df_ventas.describe(include='all')` — estadísticas descriptivas.

3. Detección de duplicados  
   - Duplicados totales: 0
   - Duplicados por id_venta: 0
   - Visualización de duplicados exactos: 0 
    

4. Valores nulos y tipos  

   - Conteo de nulos por columna: 
id_venta          0
fecha             0
id_cliente        0
nombre_cliente    0
email             0
medio_pago        0
dtype: int64

   - Revisión de dtypes: 
id_venta                   int64
fecha             datetime64[ns]
id_cliente                 int64
nombre_cliente            object
email                     object
medio_pago                object
dtype: object

5. Conteo de filas y columnas  
   - Filas: 120
   - Columnas: 6

## Resultados obtenidos
- Filas totales: <pegar salida de `df_ventas.shape[120]`>  
- Columnas totales: <pegar salida de `df_ventas.shape[6]`>  
- Nulos por columna:  
  - id_venta: 0  
  - fecha: 0  
  - id_cliente: 0  
  - nombre_cliente: 0  
  - email: 0  
  - medio_pago: 0  
 

- Primeras filas (muestra): insertar `df_ventas.head(10)` si se desea ejemplo de formatos/errores.


## Acciones recomendadas (siguientes pasos)
1. Convertir columnas de fecha con `pd.to_datetime` y validar rangos (fechas futuras).  
2. Corregir o eliminar duplicados según regla de negocio.  
3. Imputar o eliminar nulos según importancia de la columna.  
4. Verificar montos negativos o cero (`importe`, `total`) y validar con negocio.  
5. Guardar versión documentada del dataset limpio (ej.: `ventas_limpias_v1.csv`).


````
“Los datos presentan buena calidad general, sin duplicados ni nulos, lo que permite avanzar al análisis exploratorio y generación de gráficos.”