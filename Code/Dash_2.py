#!/usr/bin/env python
# coding: utf-8

# In[14]:


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Cargar tu DataFrame
def load_data_2():
    data_ind = pd.read_excel(r'/home/ubuntu/prec/data/PCA_ncomp_1.xlsx', sheet_name='Sheet1')
    data_ind['Fecha'] = pd.to_datetime(data_ind['Fecha'])
    data_ind = data_ind.set_index("Fecha")
    return data_ind
# Cargar datos
df = load_data_2()

# Iniciar la aplicación Dash
app = dash.Dash(__name__)

# Crear opciones para los filtros
entidades_opciones = [{'label': entidad, 'value': entidad} for entidad in df['Entidad'].unique()]
years_opciones = [{'label': year, 'value': year} for year in df.index.year.unique()]

# Diseño de la aplicación
app.layout = html.Div([
    html.H1("Tendencia del Indicador del Riesgo"),
    dcc.Dropdown(
        id='entidad-selector',
        options=entidades_opciones,
        multi=True,
        value=[entidades_opciones[0]['value']],  # Valor predeterminado es la primera entidad
        style={'width': '50%'}
    ),
    dcc.Dropdown(
        id='year-selector',
        options=years_opciones,
        multi=True,
        value=[years_opciones[0]['value']],  # Valor predeterminado es el primer año
        style={'width': '50%'}
    ),
    dcc.Graph(id='scatter-plot'),
])

# Callback para actualizar el gráfico
@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('entidad-selector', 'value'),
     Input('year-selector', 'value')]
)
def update_graph(selected_entidades, selected_years):
    # Filtrar el DataFrame según las entidades seleccionadas y los años seleccionados
    df_filtered = df[(df['Entidad'].isin(selected_entidades)) & (df.index.year.isin(selected_years))]

    # Crear el gráfico actualizado
    fig = px.line(df_filtered, x=df_filtered.index, y='Indicador', color='Entidad',
                  title="Seleccione una o varias entidades bancarias, y uno o varios años con los filtros de arriba, y observe el comportamiento en el tiempo del indicador de riesgo.",
                  labels={'Indicador': 'Valor del Indicador de Riesgo', 'Fecha': 'Fecha'})
    return fig

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(port=8050)

