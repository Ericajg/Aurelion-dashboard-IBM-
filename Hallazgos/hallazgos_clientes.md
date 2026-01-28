# Inspección Inicial - Dataset Clientes

Fecha: 28 de octubre de 2025
Archivo analizado: clientes.xlsx
Notebook: limpieza_clientes.ipynb

"Este dataset contiene la información de los clientes de una empresa, incluyendo datos personales y fecha de alta. El objetivo del análisis es evaluar la calidad de los registros y preparar la base para el análisis de comportamiento de clientes"

## Pasos Realizados

1. Configuración del Entorno
   - Importación de librerías (pandas)
   - Verificación y cambio del directorio de trabajo
   - Comprobación de archivos disponibles

2. Carga de Datos
   - Lectura del archivo Excel "clientes.xlsx"
   - Vista previa con df_clientes.head()

3. Análisis Exploratorio
   - Información general del DataFrame (df_clientes.info())
   - Estadísticas descriptivas (df_clientes.describe())
   
4. Validación de Calidad
   - Búsqueda de duplicados totales y por id_cliente
   - Detección de valores nulos
   - Revisión de tipos de datos
   - Validación de fechas futuras

## Estructura de Datos

- Total de filas: [ df_clientes.shape[0]] 100
- Total de columnas: [ df_clientes.shape[1]] 5
- Columnas presentes:
  - id_cliente
  - fecha_alta
  - nombre_cliente
  - email
  - ciudad

## Resultados del Análisis

### Valores Nulos
df_clientes.isnull().sum(): 
id_cliente        0
nombre_cliente    0
email             0
ciudad            0
fecha_alta        0
dtype: int64

### Duplicados
- Filas duplicadas completas: [0]
- IDs de cliente duplicados: [0]

### Tipos de Datos
[df_clientes.dtypes]
id_cliente                 int64
nombre_cliente            object
email                     object
ciudad                    object
fecha_alta        datetime64[ns]
dtype: object

# duplicados completos
duplicados_exactos = df_clientes[df_clientes.duplicated(keep=False)]
duplicados_exactos.shape : [0]

### Validación de Fechas
- Registros con fechas posteriores a 27/10/2025: [0]

## Problemas Detectados
- No se detectaron anomalías en esta fase de inspección.


## Acciones Recomendadas
- Ninguna por el momento. Continuar con la siguiente etapa de limpieza.

## Próximos Pasos
- Tratamiento de valores nulos
- Corrección de tipos de datos
- Eliminación/tratamiento de duplicados
- Validación de fechas incorrectas

---
- No se detectaron anomalías en esta fase de inspección.

## Conclusión General
La base de datos de clientes presenta buena calidad.
No se detectaron registros duplicados ni valores faltantes.
Todas las variables están correctamente tipificadas y las fechas son válidas.
Los datos están listos para integrarse con las bases de ventas y facturación para el análisis general.
