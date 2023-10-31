#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as mp


# In[4]:


datos = pd.read_excel(r'/home/ubuntu/prec/data/data.xlsx', sheet_name='Datos')
datos.head(5)


# In[10]:


datos = datos.set_index('Fecha')


# # Descripción de los datos

# In[11]:


datos.shape


# In[12]:


AtributosNumericos = datos.columns
AtributosNumericos = AtributosNumericos[1:]
print(AtributosNumericos)


# In[13]:


Estadisticas = pd.DataFrame(datos)
print(Estadisticas.describe())


# In[14]:


sns.pairplot(datos, kind="scatter")
plt.show()


# In[15]:


correlation_matrix = datos.corr()
dataplot = sns.heatmap(datos.corr(), cmap="YlGnBu", annot=True)
# displaying heatmap
mp.show()
print(correlation_matrix)


# In[16]:


for i in AtributosNumericos:
  sns.catplot(data=datos, y=i, kind="box",margin_titles=True)
  sns.displot(datos, x=i, kind="kde",fill=True,common_norm=False)


# **A partir del cuadro podemos mencionar las siguientes conclusiones:**
# 
# **Utilidad/ingresos vs. ROA y ROE:** Existe una correlación lineal positiva muy fuerte entre la utilidad como proporción de los ingresos y las medidas de rentabilidad ROA y ROE. Esto sucede pues a mayores utilidades es de esperarse que también se incrementen estas medidas pues también tienen de numerador a las utilidades.
# **Cartera/Depósitos vs. Gast_Op/Activos:** Existe una correlación lineal positiva (0.57) entre la relación Cartera/Depósitos y el gasto operativo como proporción de los activos. Esto sugiere que a medida que la proporción de cartera aumenta, el gasto operativo también aumenta.
# **Cartera/Activos vs. solvencia e IRL:** Si una entidad está muy expuesta a cartera su solvencia e IRL se ven reducidos.
# **Cartera/Activos, Cartera/Depósitos y calidad:**  entre más expuesta esté una entidad a cartera también está expuesta a que hayan más incumplimiento por deudores y por ende el indicador de calidad puede incrementar
# 
# 
# 
# 
# 
