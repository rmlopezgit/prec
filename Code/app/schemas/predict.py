from typing import Any, List, Optional

from pydantic import BaseModel
class DataInputSchema(BaseModel):
    Entidad: Optional[str]
    Fecha: Optional[str]
    Solvencia: Optional[float]
    IRL: Optional[float]
    Cartera_Depósitos: Optional[float]
    Cartera_Activos: Optional[float]
    Gast_ope_Activos: Optional[float]
    ROA: Optional[float]
    ROE: Optional[float]
    Calidad: Optional[float]
    Utilidad_Ingresos: Optional[float]

# Esquema de los resultados de predicción
class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    predictions: Optional[Any]

# Esquema para inputs múltiples
class MultipleDataInputs(BaseModel):
    inputs: List[DataInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "Entidad": "BANCAMÍA S. A.",
                        "Fecha": "2023-10-01 00:00:00",
                        "Solvencia": 4.4,
                        "IRL": 52.1,
                        "Cartera_Depósitos": 12.8,
                        "Cartera_Activos": 80.5,
                        "Gast_ope_Activos": 58.6,
                        "ROA": 52.3,
                        "ROE": 2.5,
                        "Calidad": 3.6,
                        "Utilidad_Ingresos": 2.8
                    }
                ]
            }
        }
