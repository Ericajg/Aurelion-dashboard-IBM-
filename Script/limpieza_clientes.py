#!/usr/bin/env python
# coding: utf-8

# In[6]:


import os
import pandas as pd

# Nos movemos a la carpeta donde están los archivos Excel
os.chdir(r'C:\Users\Yo\OneDrive\Desktop\IA\ProyectoAurelion_EricaAlmiron')


# In[8]:


# Cargamos los clientes
df_clientes = pd.read_excel(r"C:\Users\Yo\OneDrive\Desktop\IA\ProyectoAurelion_EricaAlmiron\datos_originalesAurelion\clientes.xlsx")
df_clientes.head()


# In[9]:


# 🔍 Información general del DataFrame 
#    Paso 1: Inspección inicial de los datos
df_clientes.info()


# In[10]:


# 📊 Estadísticas descriptivas de las columnas
df_clientes.describe(include='all')


# In[11]:


df_clientes.duplicated().sum()


# In[12]:


#revisar solo un campo clave (por ejemplo email
df_clientes['id_cliente'].duplicated().sum()


# In[13]:


#Buscar valores nulos
df_clientes.isnull().sum()


# In[14]:


# ver filas duplicadas exactas
duplicados_exactos = df_clientes[df_clientes.duplicated(keep=False)]
duplicados_exactos.shape


# In[15]:


#Revisar tipos de datos (dtypes)
df_clientes.dtypes


# In[16]:


#validar fechas futuras
df_clientes[df_clientes['fecha_alta'] > '2025-10-27']  # fecha actual


# In[17]:


#total filas
df_clientes.shape[0]


# In[18]:


#total columnas
df_clientes.shape[1]


# In[19]:


# Ver las primeras filas para confirmar que todo está bien
df_clientes.head()


# In[23]:


# 6️⃣ Guardar el archivo limpio
df_clientes.to_csv('clientes_limpios.csv', index=False, encoding='utf-8')
print("✅ Archivo limpio exportado correctamente: clientes_limpios.csv")

