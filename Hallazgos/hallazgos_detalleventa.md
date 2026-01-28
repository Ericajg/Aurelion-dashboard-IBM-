# Inspección — Primera etapa: detalle_ventas

Fecha: 28 de octubre de 2025  
Archivo analizado: detalle_ventas.xlsx  
Notebook fuente: limpieza_detalleventas.ipynb

Este dataset detalla las ventas indiciduales realizadas, incluyendo producto, cantidad, precio unitario e importee final. Es clave para validar la coherencia de los registros de facturacion y analizar patrones de consumo.

## Objetivo
Realizar la inspección inicial del dataset de detalle de ventas para detectar problemas estructurales y de calidad que requieren limpieza o transformación.

## Pasos ejecutados
1. Carga del archivo
   - Código: `pd.read_excel(r"...\detalle_ventas.xlsx")`
   - Propósito: obtener el DataFrame para las comprobaciones siguientes.

2. Inspección general
   - `df_detalle_ventas.head()` — vista previa de filas.
   - `df_detalle_ventas.info()` — tipos de columnas y presencia de nulos.
   - `df_detalle_ventas.describe(include='all')` — estadísticas descriptivas por columna.

3. Detección de duplicados
   - Duplicados completos: `df_detalle_ventas.duplicated().sum()`
   - Duplicados en clave: `df_detalle_ventas['id_venta'].duplicated().sum()`

4. Valores nulos y tipos
   - Conteo por columna: `df_detalle_ventas.isnull().sum()`
   - Tipos de datos: `df_detalle_ventas.dtypes`

5. Validaciones de consistencia numérica y temporal
   - Precios unitarios no positivos: `df_detalle_ventas[df_detalle_ventas['precio_unitario'] <= 0]`
   - Importes no positivos: `df_detalle_ventas[df_detalle_ventas['importe'] <= 0]`
   - Cantidades no positivas: `df_detalle_ventas[df_detalle_ventas['cantidad'] <= 0]`
   - (Revisar fechas fuera de rango: agregar comprobación si existe columna de fecha)

## Resultados obtenidos
> Nota: los resultados concretos (números y ejemplos) deben pegarse desde las salidas del notebook. A continuación se muestran líneas para completar con los valores reales.

- Filas totales: <`df_detalle_ventas.shape[0]`>  343
- Columnas: <`df_detalle_ventas.shape[1]` + lista de nombres de columnas> 
6 columnas (id_ventas, id_producto, nombre_producto, precio_unitario, cantidad, importe) 
- Tipos de datos (resumen):  
  - columnas numéricas: <5>  
  - columnas fecha: <->  
  - columnas objeto/texto: <1>

- Valores nulos por columna:  
  - columna_1: <0>  
  - columna_2: <0>  
  - columna_3: <0>  
  - columna_4: <0>
  - columna_5: <0>  
  - columna_6: <0>

- Duplicados:
  - duplicados completos: 0  
  - duplicados en `id_venta`: 233 (esperado, ya que una venta puede incluir varios productos)

- Registros con precio_unitario <= 0: 0  
- Registros con importe <= 0: 0
- Registros con cantidad <= 0: 0
- Fechas fuera de rango (si aplica): no aplica


🟩 Conclusión final

El dataset de detalle_ventas presenta una estructura consistente y sin valores nulos o importes negativos. Los duplicados en la columna id_venta son esperables, ya que un mismo identificador de venta puede incluir varios productos asociados.
En general, los datos se consideran limpios y listos para el análisis, conservando coherencia entre cantidad, precio unitario e importe