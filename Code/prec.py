#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as mp


# In[19]:


datos = pd.read_excel(open('/home/ubuntu/prec/data/data.xlsx', 'rb'), sheet_name='Datos')
datos.head(5)


# # Descripción de los datos

# In[31]:


datos.shape


# In[38]:


AtributosNumericos = datos.columns
AtributosNumericos = AtributosNumericos[1:]
print(AtributosNumericos)


# In[39]:


Estadisticas = pd.DataFrame(datos)
print(Estadisticas.describe())


# In[40]:


sns.pairplot(datos, kind="scatter")
plt.show()


# In[41]:


correlation_matrix = datos.corr()
dataplot = sns.heatmap(datos.corr(), cmap="YlGnBu", annot=True)
# displaying heatmap
mp.show()
print(correlation_matrix)


# In[42]:


for i in AtributosNumericos:
  sns.catplot(data=datos, y=i, kind="box",margin_titles=True)
  sns.displot(datos, x=i, kind="kde",fill=True,common_norm=False)


# 
# Para hacer el análisis preliminar nos aproyamos de diagramas de cajas y bigotes, densidad, dispersión junto con el uso de estadísticas descriptivas y de correlación lineal entre las variables con lo que se llegó a las siguientes conclusiones:
# 
# > **Utilidad/ingresos vs. ROA:** Existe una correlación lineal positiva muy fuerte (0.97) entre la utilidad como proporción de los ingresos y el retorno de activos (ROA). Esto sugiere que a medida que el ROA aumenta, la empresa tiende a generar una mayor utilidad en relación con sus ingresos.
# 
# > **Cartera/Depósitos vs. Gast_Op/Activos:** Existe una correlación lineal negativa fuerte (-0.87) entre la relación Cartera/Depósitos y el gasto operativo como proporción de los activos. Esto sugiere que a medida que la proporción de cartera de préstamos con respecto a los depósitos aumenta, el gasto operativo como proporción de los activos tiende a disminuir significativamente.
# 
# > **Gast_Op/Activos:** La variabilidad en esta relación es moderada, y la media indica que, en promedio, las instituciones gastan aproximadamente el 4.80% de sus activos en gastos operativos.
# 
# > **ROA (Return on Assets) y ROE (Return on Equity):** Ambas variables tienen medias positivas, lo que indica que, en promedio, las instituciones son rentables en términos de activos y patrimonio. Sin embargo, la variabilidad en estas tasas es alta, y hay observaciones con rendimientos negativos, especialmente en ROE como lo es por ejemplo para el caso del banco Pichincha S.A.
# 
# Estas variables nos pueden ser útiles para calcular el riesgo de las instituciones financieras, ya que ofrecen una visión de diferentes aspectos de su salud financiera, como por ejemplo:
# 
# > **Solvencia:** Mide la capacidad de una institución financiera para cumplir con sus obligaciones financieras a medida que vencen. Un bajo nivel de solvencia podría indicar un mayor riesgo de incumplimiento. Esta variable es fundamental para evaluar el riesgo crediticio.
# 
# > **IRL (Ingresos / Recursos Líquidos):** Un IRL alto sugiere una mejor capacidad para generar ingresos con los recursos disponibles, lo que puede reducir el riesgo financiero.
# 
# > **Cartera/Depósitos y Cartera/Activos:** Estas relaciones son relevantes para evaluar el riesgo de concentración de activos y la calidad de la cartera de préstamos. Un alto ratio de Cartera/Depósitos puede indicar una dependencia significativa de los préstamos en relación con los depósitos, lo que podría aumentar el riesgo si los préstamos no son de alta calidad. Por otro lado, un bajo ratio de Cartera/Activos podría señalar una mayor diversificación de activos, lo que podría reducir el riesgo.
# 
# > **Gast_Op/Activos:** Esta variable proporciona información sobre la eficiencia operativa de la institución financiera. Un alto nivel de gastos operativos en relación con los activos podría indicar ineficiencias y aumentar el riesgo de rentabilidad.
# 
# En resumen, estas variables proporcionan una visión integral de la salud financiera de las instituciones financieras y son fundamentales para evaluar el riesgo en diferentes aspectos, como el riesgo crediticio, el riesgo operativo y el riesgo de rentabilidad.
# 
# 
# 
# 
# 
