#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# Cargamos las ventas
df_ventas = pd.read_excel(r"C:\Users\Yo\OneDrive\Desktop\IA\ProyectoAurelion_EricaAlmiron\datos_originalesAurelion\ventas.xlsx")


# In[3]:


# Mostrar las primeras 10 filas del DataFrame
df_ventas.head(10)


# In[4]:


# 🔍 Información general del DataFrame 
#    Paso 1: Inspección inicial de los datos
df_ventas.info()


# In[5]:


# 📊 Estadísticas descriptivas de las columnas
df_ventas.describe(include='all')


# In[6]:


#duplicados en todo el DataFrame
df_ventas.duplicated().sum()


# In[7]:


#duplicados en `id_venta`
df_ventas['id_venta'].duplicated().sum()


# In[8]:


#Buscar valores nulos
df_ventas.isnull().sum()


# In[9]:


# ver filas duplicadas exactas
duplicados_exactos = df_ventas[df_ventas.duplicated(keep=False)]
duplicados_exactos.shape


# In[10]:


#Revisar tipos de datos (dtypes)
df_ventas.dtypes


# In[12]:


#total filas
df_ventas.shape[0]


# In[13]:


#total columnas
df_ventas.shape[1]


# In[16]:


# 6️⃣ Guardar el archivo limpio
df_ventas.to_csv('ventas_limpios.csv', index=False, encoding='utf-8')
print("✅ Archivo limpio exportado correctamente: ventas_limpios.csv")

