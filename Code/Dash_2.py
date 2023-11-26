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
    data_ind = pd.read_excel(r'C:/Users/dmonroy3/Desktop/Notebooks/PCA_ncomp_1.xlsx', sheet_name='Sheet1')
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
app.layout = html.Div(style={'font-family': 'Arial', 'backgroundColor': '#f0f0f0', 'height': '100vh'}, children=[
    html.H1("Tendencia del Indicador de Riesgo Financiero", style={'textAlign': 'center', 'color': '#154c79', 'margin-bottom': '0'}),
    html.H2("Universidad de los Andes", style={'textAlign': 'center', 'color': '#154c79', 'margin-top': '0', 'margin-bottom': '0'}),
    html.H3("Grupo 2 DSA", style={'textAlign': 'center', 'color': '#154c79', 'margin-top': '0', 'margin-bottom': '20px'}),
    html.P("Aplicación Dash interactiva que permite seleccionar entidades bancarias y años para visualizar la tendencia del indicador de riesgo financiero.", style={'textAlign': 'center', 'margin-bottom': '20px'}),
    
    # Nueva sección para la solvencia
    html.Div([
        html.Label("Solvencia", style={'margin-right': '10px', 'fontSize': '17px', 'fontWeight': 'bold'}),
        dcc.Input(
            id='solvencia-input',
            type='number',
            value=0,  # Puedes establecer el valor predeterminado que desees
            style={'width': '5%'}
        ),
        html.Label("IRL", style={'margin-right': '10px', 'fontSize': '17px', 'fontWeight': 'bold'}),
        dcc.Input(
            id='irl-input',
            type='number',
            value=0,  # Puedes establecer el valor predeterminado que desees
            style={'width': '5%'}
        ),
        html.Label("Cartera_Depósitos", style={'margin-right': '10px', 'fontSize': '17px', 'fontWeight': 'bold'}),
        dcc.Input(
            id='Cartera_Depósitos-input',
            type='number',
            value=0,  # Puedes establecer el valor predeterminado que desees
            style={'width': '5%'}
        ),
        html.Label("Cartera_Activos", style={'margin-right': '10px', 'fontSize': '17px', 'fontWeight': 'bold'}),
        dcc.Input(
            id='Cartera_Activos-input',
            type='number',
            value=0,  # Puedes establecer el valor predeterminado que desees
            style={'width': '5%'}
        ),
        html.Label("Gast_ope_Activos", style={'margin-right': '10px', 'fontSize': '17px', 'fontWeight': 'bold'}),
        dcc.Input(
            id='Gast_ope_Activos-input',
            type='number',
            value=0,  # Puedes establecer el valor predeterminado que desees
            style={'width': '5%'}
        ),
        html.Label("ROA", style={'margin-right': '10px', 'fontSize': '17px', 'fontWeight': 'bold'}),
        dcc.Input(
            id='ROA-input',
            type='number',
            value=0,  # Puedes establecer el valor predeterminado que desees
            style={'width': '5%'}
        ),
        html.Label("ROE", style={'margin-right': '10px', 'fontSize': '17px', 'fontWeight': 'bold'}),
        dcc.Input(
            id='ROE-input',
            type='number',
            value=0,  # Puedes establecer el valor predeterminado que desees
            style={'width': '5%'}
        ),
        html.Label("Calidad", style={'margin-right': '10px', 'fontSize': '17px', 'fontWeight': 'bold'}),
        dcc.Input(
            id='Calidad-input',
            type='number',
            value=0,  # Puedes establecer el valor predeterminado que desees
            style={'width': '5%'}
        ),
        html.Label("Utilidad_Ingresos", style={'margin-right': '10px', 'fontSize': '17px', 'fontWeight': 'bold'}),
        dcc.Input(
            id='Utilidad_Ingresos-input',
            type='number',
            value=0,  # Puedes establecer el valor predeterminado que desees
            style={'width': '5%'}
        ),
        html.Label("Entidad_Ban", style={'margin-right': '10px', 'fontSize': '17px', 'fontWeight': 'bold'}),
        dcc.Input(
            id='Entidad_Ban-input',
            type='str',
            value=0,  # Puedes establecer el valor predeterminado que desees
            style={'width': '5%'}
        ), 
        html.Label("Fecha", style={'margin-right': '10px', 'fontSize': '17px', 'fontWeight': 'bold'}),
        dcc.Input(
            id='Fecha-input',
            type='str',
            value=0,  # Puedes establecer el valor predeterminado que desees
            style={'width': '5%'}
        ),       
    ], style={'display': 'flex', 'justifyContent': 'center', 'margin-bottom': '20px'}),
    
    html.Div([
        html.Label("Entidad", style={'margin-right': '10px', 'fontSize': '17px', 'fontWeight': 'bold'}),
        dcc.Dropdown(
            id='entidad-selector',
            options=entidades_opciones,
            multi=True,
            value=[entidades_opciones[0]['value']],
            style={'width': '40%', 'margin-right': '10%'}
        ),
        html.Label("Año", style={'margin-right': '10px', 'fontSize': '17px', 'fontWeight': 'bold'}),
        dcc.Dropdown(
            id='year-selector',
            options=years_opciones,
            multi=True,
            value=[years_opciones[0]['value']],
            style={'width': '40%'}
        ),
    ], style={'display': 'flex', 'justifyContent': 'center', 'margin-bottom': '5px'}),
    dcc.Graph(
        id='scatter-plot',
        style={'backgroundColor': '#87CEEB', 'height': '80vh'}
    ),
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

    # Crear el gráfico actualizado con el estilo del fondo cambiado
    fig = px.line(df_filtered, x=df_filtered.index, y='Indicador', color='Entidad',
    labels={'Indicador': 'Valor del Indicador de Riesgo', 'Fecha': 'Fecha'})

    # Modificar el estilo del fondo del gráfico
    fig.update_layout(
        plot_bgcolor='#D6EAF8',  # Cambiar el fondo del gráfico a un tono azul cielo
        paper_bgcolor='#f0f0f0',  # Cambiar el fondo del papel (parte externa del gráfico)
    )

    return fig

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(port=8050)
