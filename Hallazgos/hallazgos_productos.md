# Inspección — Primera etapa: tabla productos

Fecha: 28 de octubre de 2025  
Archivo analizado: productos.xlsx  
Notebook fuente: limpieza_productos.ipynb

## Objetivo
Inspeccionar la tabla de productos para identificar problemas de calidad y estructura antes de la limpieza.

## Pasos realizados
1. Carga de datos  
   - Código: `df_productos = pd.read_excel(r"...\productos.xlsx")`  
   - Vista previa: `df_productos.head()`

2. Inspección general  
   - `df_productos.info()` — tipos, nulos y memoria.  
   - `df_productos.describe(include='all')` — estadísticas por columna.

3. Duplicados  
   - Duplicados completos: `df_productos.duplicated().sum()`  
   - Duplicados en clave (ej. `id_producto`): `df_productos['id_producto'].duplicated().sum()`

4. Valores nulos y tipos  
   - Conteo nulos por columna: `df_productos.isnull().sum()`  
   - Tipos de columnas: `df_productos.dtypes`

5. Validaciones de consistencia numérica y categórica  
   - Precios no positivos: `df_productos[df_productos['precio'] <= 0]`  
   - Stock negativo: `df_productos[df_productos['stock'] < 0]`  
   - Categorías inesperadas / valores únicos: `df_productos['categoria'].value_counts()`

6. Ejemplos de problemas detectados  
   - Mostrar filas problemáticas con `.head(10)` para cada chequeo.

## Resultados 
- Filas totales: 100  
- Columnas: 4 
 lista de nombres de columnas>
 - id_producto
 - nombre_producto
 - categoria
 - precio_unitario

- Tipos de datos (resumen):  
  - columnas numéricas: <2>  
  - columnas fecha: <no aplica>  
  - columnas texto: <2>

- Valores nulos por columna:  0
 

- Duplicados:
  - duplicados completos: <0>  
  - duplicados en `id_producto`: <0>

- Registros con `precio` <= 0: <0>  
 
- Categorías no esperadas o valores únicos: <2>


🟩 Conclusión final

El dataset de productos presenta una estructura ordenada y coherente. No se detectaron valores nulos, duplicados ni precios negativos.
Las categorías se encuentran correctamente definidas y los precios resultan consistentes con el tipo de producto.
En consecuencia, este conjunto de datos se considera limpio y validado, apto para integrarse con las demás tablas del modelo de análisis (ventas, detalle_ventas y clientes).

---
