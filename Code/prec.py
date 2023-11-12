#!/usr/bin/env python
# coding: utf-8

# In[6]:


# librerías:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as mp
import mlflow
from scipy.cluster.hierarchy import linkage, fcluster
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score


# In[9]:


datos = pd.read_excel(r'/home/ubuntu/prec/data/data.xlsx', sheet_name='Datos')
#datos = pd.read_excel(r'C:/Users/rlope/Downloads/data.xlsx', sheet_name='Datos')
datos.head(5)


# # Descripción de los datos

# In[ ]:


datos.shape


# In[ ]:


AtributosNumericos = datos.columns
AtributosNumericos = AtributosNumericos[1:]
print(AtributosNumericos)


# In[ ]:


Estadisticas = pd.DataFrame(datos)
print(Estadisticas.describe())


# In[ ]:


sns.pairplot(datos, kind="scatter")
plt.show()


# In[ ]:


correlation_matrix = datos.corr()
dataplot = sns.heatmap(datos.corr(), cmap="YlGnBu", annot=True)
# displaying heatmap
mp.show()
print(correlation_matrix)


# In[ ]:


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

# In[ ]:


datos = datos.set_index('Fecha')


# In[ ]:


# Se defienen las x como la base sin las dos primeras columnas:

x = datos.iloc[:, 2:]
x


# In[ ]:


# Estandarizamos las variables para que no influyan las distintas medidas:

scaler = StandardScaler()
x_estandarizado = scaler.fit_transform(x)
x_estandarizado


# In[ ]:


# Se tienen entonces 145 observaciones para 9 variables estandarizadas:

print(len(x_estandarizado[0]))
print(len(x_estandarizado))


# In[ ]:


methods = ['single', 'complete', 'average', 'centroid','ward']


# In[ ]:


# registre el experimento
experiment = mlflow.set_experiment("Experimientos de Clusters indicadores de Riesgo")


# In[ ]:


for method in methods:
    
    with mlflow.start_run(experiment_id=experiment.experiment_id):
        # defina los parámetros del modelo
        # Configurar y aplicar PCA:
        n_components = 0.80  # Retener el 80% de la varianza.
        pca = PCA(n_components=n_components, svd_solver='full', random_state=0)
        pca.fit(x_estandarizado)

        # Ajustar PCA a los datos originales y transformarlos
        x_reduced = pca.fit_transform(x_estandarizado)

        distances = linkage(x_reduced, method=method, metric="euclidean")
        clusters = fcluster(distances, 3, criterion="distance")
        plt.title('linkage: ' + method)
        plt.scatter(x_reduced[:,0], x_reduced[:,1], c=clusters, cmap='tab20b')
        plt.show()
        score_7 = silhouette_score(x_reduced, clusters)
        print(f"Silhouette Score: {score_7}")

        # Registre los parámetros
        mlflow.log_param("Metodo", method)

        # Cree y registre la métrica de interés
        mlflow.log_metric("Silhouette core", score_7)
        print(score_7)

        mlflow.log_param("Varianza explicada para PCA", n_components)

