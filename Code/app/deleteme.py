import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Crear el DataFrame
data = {
    'Indicador': [-8.317217852, 1.24313181, 1.15578049, 1.029202947],
    'Indicador2': [13.83927836, 3.413537449, 3.17551513, 3.081945133],
    'Fecha': ['2023-10-01', '2018-01-01', '2018-02-01', '2018-03-01'],
    'Entidad': ['BANCAMÍA S. A.', 'BANCAMÍA S. A.', 'BANCAMÍA S. A.', 'BANCAMÍA S. A.'],
    'Cluster': [10, 8, 8, 8]
}

df = pd.DataFrame(data)

# Convertir la columna 'Fecha' al tipo de dato datetime
df['Fecha'] = pd.to_datetime(df['Fecha'])

# Obtener la lista única de entidades y años
entidades = df['Entidad'].unique()
años = df['Fecha'].dt.year.unique()

# Inicializar la aplicación Dash
app = dash.Dash(__name__)

# Diseño de la aplicación
app.layout = html.Div([
    html.H1("Gráfico de Clusters"),

    # Dropdown para seleccionar la entidad
    dcc.Dropdown(
        id='dropdown-entidad',
        options=[{'label': entidad, 'value': entidad} for entidad in entidades],
        value=entidades[0],
        multi=False,
        style={'width': '50%'}
    ),

    # Dropdown para seleccionar el año
    dcc.Dropdown(
        id='dropdown-año',
        options=[{'label': año, 'value': año} for año in años],
        value=años[0],
        multi=False,
        style={'width': '50%'}
    ),

    dcc.Graph(id='scatter-plot'),

])

# Callback para actualizar el gráfico
@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('dropdown-entidad', 'value'),
     Input('dropdown-año', 'value')]
)
def update_graph(selected_entidad, selected_año):
    # Filtrar el DataFrame por entidad y año seleccionados
    filtered_df = df[(df['Entidad'] == selected_entidad) & (df['Fecha'].dt.year == selected_año)]

    # Crear el gráfico de dispersión
    fig = px.scatter(
        filtered_df,
        x='Indicador',
        y='Indicador2',
        color='Cluster',
        hover_name='Entidad',
        title=f'Gráfico de Clusters para {selected_entidad} en {selected_año}'
    )

    return fig

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)