from multiprocessing import connection
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate


import plotly.graph_objects as go
import plotly.express as px
import sqlite3
import pandas as pd
import plotly.figure_factory as ff

app = dash.Dash()  # initialising dash app
connexion = sqlite3.connect('table_repro_IS.db')


def DistplotsFUN(chosenYearMin, chosenYearMax, chosenStation):
    query = "SELECT * FROM recolte WHERE {} >= {} AND {} <= {} AND {} = {} ".format(
        'Year', chosenYearMin, 'Year', chosenYearMax, 's_id', chosenStation)
    fig = px.histogram(
        query, x=query["VH"], y=query["Ntot"], color=query["Station"], marginal="rug")
    return fig


df_station = pd.read_sql_query(
    '''SELECT * FROM station''', connexion)


html.Div([
    dcc.Checklist(
        id='checklist',
        options=[
            {'label': x, 'value': x, 'disabled': False} for x in df_station['Station'].unique()
        ],
        value=['Josbaig'],  # values chosen by default
    )
])


@ app.callback(
    Output(omponent_id='', component_property='figure'),
    [Input(component_id='checklist', component_property='value')]
)

def update_graph(selected_station):
    dff = df_station[df_station['Station'].isin(selected_station)]
    print(dff['Station'].unique())

    displot = ff.create_distplot(
        [dff[c] for c in dff.columns], dff.columns, bin_size=.25)

    return displot


if __name__ == '__main__':
    app.run_server(debug=True)
