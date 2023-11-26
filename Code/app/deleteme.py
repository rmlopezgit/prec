import requests
import json

myreq = {
  "inputs": [
    {
      "Entidad": "Loca",
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
headers =  {"Content-Type":"application/json", "accept": "application/json"}
response = requests.post('http://127.0.0.1:8001/api/v1/predict', data=json.dumps(myreq), headers=headers)