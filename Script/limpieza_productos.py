#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[5]:


# Cargamos los productos
df_productos = pd.read_excel(r"C:\Users\Yo\OneDrive\Desktop\IA\ProyectoAurelion_EricaAlmiron\datos_originalesAurelion\productos.xlsx")
df_productos.head(10)


# In[3]:


# 🔍 Información general del DataFrame 
#    Paso 1: Inspección inicial de los datos
df_productos.info()


# In[4]:


# 📊 Estadísticas descriptivas de las columnas
df_productos.describe(include='all')


# In[5]:


#duplicados en todo el DataFrame
df_productos.duplicated().sum()


# In[6]:


#duplicados en `id_producto`
df_productos['id_producto'].duplicated().sum()


# In[7]:


#Buscar valores nulos
df_productos.isnull().sum()


# In[8]:


df_productos['categoria'].value_counts()


# In[12]:


# ver filas duplicadas exactas
duplicados_exactos = df_productos[df_productos.duplicated(keep=False)]
duplicados_exactos.shape


# In[13]:


#Revisar tipos de datos (dtypes)
df_productos.dtypes


# In[14]:


#validar precios negativos
df_productos[df_productos['precio_unitario'] < 0]



# In[15]:


#total filas
df_productos.shape[0]


# In[16]:


#total columnas
df_productos.shape[1]


# In[7]:


# 6️⃣ Guardar el archivo limpio
df_productos.to_csv('productos_limpios.csv', index=False, encoding='utf-8')
print("✅ Archivo limpio exportado correctamente: productos_limpios.csv")


# In[ ]:




