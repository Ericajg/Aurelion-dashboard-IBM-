📊 Hallazgos – Dataset Unificado Aurelion

1. Introducción

En esta etapa del proyecto se trabajó con un dataset unificado, resultante de la integración de las tablas de clientes, ventas, detalle de ventas y productos.
Previo al análisis, se realizó una corrección manual de la columna categoría, ya que se detectaron productos mal clasificados entre Alimentos y Limpieza, lo cual afectaba directamente los análisis previos.

A partir de esta tabla única y corregida, se generaron nuevos análisis y visualizaciones, descartando los gráficos anteriores basados en tablas separadas.

2. KPIs Generales

Como primer acercamiento al comportamiento del negocio, se calcularon los siguientes indicadores clave:

💰 Ventas totales: $2,651,417

📊 Venta promedio por operación: $7,730.08

🧾 Cantidad total de ventas: 120

👤 Cliente con mayor gasto: Agustina Flores

Estos KPIs permiten dimensionar el volumen general de ventas y sirven como base para los análisis posteriores.

3. Evolución de Ventas Mensuales

El análisis temporal muestra el comportamiento de las ventas entre enero y junio:

📉 Abril registra el menor nivel de ventas con $254,524.

📈 Mayo presenta un fuerte crecimiento, alcanzando el pico máximo con $561,832.

Este salto significativo entre abril y mayo sugiere un posible efecto estacional, acciones comerciales puntuales o cambios en la demanda que deberían ser analizados con mayor profundidad en futuras etapas.

4. Ventas por Categoría

Luego de la corrección de categorías, se observa una clara diferencia entre ellas:

🥫 Alimentos: $2,214,681

🧴 Limpieza: $436,736

La categoría Alimentos concentra la mayor parte de la facturación, representando la actividad principal del negocio, mientras que Limpieza funciona como una categoría complementaria.

5. Productos Más Vendidos

El ranking de productos por importe total revela una concentración clara en algunos artículos:

Desodorante Aerosol: $93,600

Queso Rallado: $89,544

Pizza Congelada: $85,720

Luego continúan productos como ron, yerba mate y otros alimentos de consumo frecuente.

Esto indica que tanto productos de higiene personal como alimentos procesados tienen un peso relevante en las ventas.

6. Clientes con Mayor Gasto

El análisis de los clientes muestra que el gasto no está distribuido de manera uniforme:

🥇 Cliente 1: $132,158

🥈 Cliente 2: $118,790

🥉 Cliente 3: $90,701

Existe una concentración del gasto en un grupo reducido de clientes, lo que puede representar una oportunidad para estrategias de fidelización.

7. Ventas por Región y Categoría

El análisis geográfico evidencia diferencias claras entre ciudades:

Río Cuarto lidera las ventas en ambas categorías, con una diferencia marcada respecto al resto.

Alta Gracia ocupa el segundo lugar en Alimentos, pero no en Limpieza.

Luego se ubican Córdoba Capital, Villa María, Carlos Paz y Mendiolaza.

Este comportamiento sugiere que Río Cuarto es una plaza estratégica para el negocio.

8. Medios de Pago

La distribución de los medios de pago muestra las preferencias de los clientes:

💵 Efectivo: 32.4%

📱 QR: 26.5%

🔁 Transferencia: 21%

💳 Tarjeta: 20.1%

El efectivo continúa siendo el medio predominante, aunque los pagos digitales (QR y transferencias) tienen una participación muy significativa.

9. Análisis Estadístico y Outliers

El análisis de la distribución de importes y el boxplot permitió identificar:

🚨 7 valores atípicos (outliers)

Estos valores corresponden a importes considerablemente más altos que el promedio, y probablemente estén asociados a compras de mayor volumen o clientes con consumo excepcionalmente alto.

10. Análisis de Correlación

La matriz de correlación muestra las siguientes relaciones:

Cantidad – Importe: correlación positiva moderada (0.60)

Precio Unitario – Importe: correlación positiva (0.68)

Cantidad – Precio Unitario: correlación muy baja (0.07)

Esto indica que el importe total está más influenciado por la cantidad y el precio unitario que por una relación directa entre ambos, lo cual es coherente con el comportamiento esperado en ventas.

11. Conclusión General

El análisis del dataset unificado permitió obtener una visión más clara y confiable del negocio.
La corrección de categorías fue clave para evitar interpretaciones erróneas, y los resultados muestran:

Predominio de la categoría Alimentos.

Fuerte concentración de ventas en determinados meses, productos, clientes y regiones.

Importancia creciente de medios de pago digitales.

Existencia de outliers relevantes que merecen análisis específico.

Este trabajo sienta una base sólida para la siguiente etapa del proyecto, orientada a modelos de Machine Learning y visualización interactiva en Power BI.
