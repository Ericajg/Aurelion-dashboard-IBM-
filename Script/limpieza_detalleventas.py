#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df_detalle_ventas = pd.read_excel(r"C:\Users\Yo\OneDrive\Desktop\IA\ProyectoAurelion_EricaAlmiron\datos_originalesAurelion\detalle_ventas.xlsx")
df_detalle_ventas.head()


# In[3]:


# 🔍 Información general del DataFrame 
#    Paso 1: Inspección inicial de los datos
df_detalle_ventas.info()


# In[4]:


# 📊 Estadísticas descriptivas de las columnas
df_detalle_ventas.describe(include='all')


# In[5]:


#cuántas filas completas están repetidas.
df_detalle_ventas.duplicated().sum()


# In[6]:


#revisar solo un campo clave (por ejemplo email
df_detalle_ventas['id_venta'].duplicated().sum()


# In[7]:


#Buscar valores nulos
df_detalle_ventas.isnull().sum()


# In[8]:


#Revisar tipos de datos (dtypes)
df_detalle_ventas.dtypes


# In[9]:


#validación de consistencia.  -- ¿Hay ventas con monto negativo o cero?--¿Hay fechas futuras o anteriores a la fecha mínima esperada?
df_detalle_ventas[df_detalle_ventas['precio_unitario'] <= 0]


# In[10]:


#validación de consistencia.  -- ¿Hay ventas con monto negativo o cero?--¿Hay fechas futuras o anteriores a la fecha mínima esperada?
df_detalle_ventas[df_detalle_ventas['importe'] <= 0]


# In[11]:


#validación de consistencia.  -- ¿Hay ventas con monto negativo o cero?--¿Hay fechas futuras o anteriores a la fecha mínima esperada?
df_detalle_ventas[df_detalle_ventas['cantidad'] <= 0]


# In[12]:


df_detalle_ventas.shape[0]


# In[13]:


df_detalle_ventas.shape[1]


# In[14]:


df_detalle_ventas[df_detalle_ventas['importe'] <= 0].head(10)


# In[ ]:


df_detalle_ventas.to_csv('detalle_ventas_limpios.csv', index=False)


# In[16]:


# 6️⃣ Guardar el archivo limpio
df_detalle_ventas.to_csv('detalle_ventas_limpios.csv', index=False, encoding='utf-8')
print("✅ Archivo limpio exportado correctamente: detalle_ventas_limpios.csv")

