# librerías:
from typing import Any
import pandas as pd
from scipy.cluster.hierarchy import linkage, fcluster
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
import pandas as pd
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from loguru import logger
#from model import __version__ as model_version
#from model.predict import make_prediction

import schemas
from config import settings

api_router = APIRouter()

# Ruta para verificar que la API se esté ejecutando correctamente
@api_router.get("/health", response_model=schemas.Health, status_code=200)
def health() -> dict:
    """
    Root Get
    """
    health = schemas.Health(
        name=settings.PROJECT_NAME, api_version=1.0, model_version=1.1
    )

    return health.dict()

# Ruta para realizar las predicciones
@api_router.post("/predict", response_model=schemas.PredictionResults, status_code=200)
async def predict(input_data: schemas.MultipleDataInputs) -> Any:
    """
    Prediccion usando el modelo de bankchurn
    """

    input_df = pd.DataFrame(jsonable_encoder(input_data.inputs))

    logger.info(f"Making prediction on inputs: {input_data.inputs}")
    
    #datos = pd.read_excel(r'/home/ubuntu/prec/data/data.xlsx', sheet_name='Datos')
    datos1 = pd.read_excel(r'C:/Users/rlope/Downloads/data.xlsx', sheet_name='Datos')
    input_df['Fecha'] = pd.to_datetime(input_df['Fecha'])
    datos = pd.concat([input_df, datos1], ignore_index=True)
    datos_2 = datos
    datos = datos.set_index('Fecha')
    # Se defienen las x como la base sin las dos primeras columnas:
    x = datos.iloc[:, 1:]
    # Estandarizamos las variables para que no influyan las distintas medidas:
    scaler = StandardScaler()
    x_estandarizado = scaler.fit_transform(x)
    # Configurar y aplicar PCA:
    n_components = 0.80  # Retener el 80% de la varianza.
    pca = PCA(n_components=n_components, svd_solver='full', random_state=0)
    x_reduced = pca.fit_transform(x_estandarizado)
    distances = linkage(x_reduced, method='average', metric="euclidean")
    clusters = fcluster(distances, 3, criterion="distance")
    #score_7 = silhouette_score(x_reduced, clusters)
    indicador = x_reduced[:, 1]
    indicador = pd.DataFrame(indicador)
    indicador.rename(columns={0: 'Indicador'}, inplace=True)
    indicador.rename(columns={1: 'Indicador_2'}, inplace=True)

    # Se integran los campos de Fecha y Banco de la base:
    indicador['Indicador2'] = x_reduced[:,1]
    indicador['Fecha'] = datos_2['Fecha']
    indicador['Entidad'] = datos_2['Entidad']
    indicador['Cluster'] = pd.DataFrame({'Cluster': clusters})

    #indicador.to_excel('/home/ubuntu/prec/data/PCA_ncomp_1.xlsx', index=False)
    indicador.to_excel('C:/Users/rlope/Downloads/resultados_clusterizacion.xlsx', index=False)

    results = {
        "predictions":datos.head(5),
        "errors":"NaN",
        "version":"1.0"}

    #if results["errors"] is not None:
    #    logger.warning(f"Prediction validation error: {results.get('errors')}")
    #    raise HTTPException(status_code=400, detail=json.loads(results["errors"]))

    #logger.info(f"Prediction results: {results.get('predictions')}")

    return results
