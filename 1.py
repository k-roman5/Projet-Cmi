import sqlite3

from tkinter import CENTER
from turtle import position
import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from xarray import align
import plotly.figure_factory as ff
import pandas as pd

import base64

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SKETCHY])


# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "width": "90rem",
    "padding": "2rem 1rem",
    "text-align": "center",
    "background-color": "#f8f9fa",
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
image_file_name = "simple-oak-tree-logo-design-260nw-1759587047.jpg"
encoded_image = base64.b64encode(open(image_file_name, "rb").read())

sidebar = html.Div(
    [dbc.NavLink(html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode())), href="/",
                 active="exact"),
        html.H2("CMI ISI", className="display-4",),
        html.P(
            u"Forêt Pyrénnées", className="lead"
    ),
        dbc.Nav(
            [
                dbc.NavLink("Histogramme", href="/histogramme",
                            active="exact"),
                dbc.NavLink("Tableur", href="/table",
                            active="exact"),
            ],
            horizontal=True,
            pills=True,
    ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content,
])


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    # Bar Chart
    if pathname == "/":
        return [
            html.Div(
                html.H1('welcome', id='table_view',
                        style={'textAlign': 'left'}),
            )]
    elif pathname == "/histogramme":
        #dropdown = view.GUI.build_dropdown_menu(model.data.get_unique_values())
        #graph = view.GUI.init_graph()
        return [
            html.Div([
                dcc.Checklist(
                    id='checklist',
                    options=[
                        {'label': x, 'value': x, 'disabled': False} for x in df_station['Station'].unique()
                    ],
                    value=['Josbaig'],  # values chosen by default
                )
            ])
        ]

    # Table
    elif pathname == "/table":
        # fetch client info
        return [
            html.H1('Données forêt pyrénnées (tableur)', id='table_view',
                    style={'textAlign': 'left'}),
            #html.Div(id='data_table', children=view.GUI.data_table(model.data.df))
        ]
    else:
        return html.Div(
            [
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognised..."),
            ]
        )


connexion = sqlite3.connect('table_repro_IS.db')
df_station = pd.read_sql_query(
    '''SELECT * FROM station''', connexion)


def init_scatter_plots_2():
    return dcc.Graph(id="aaaa")


def build_graph(stations):
    query = "SELECT arbre.VH, recolte.Ntot, FROM arbre JOIN recolte ON arbre.id_a=recolte.a_id WHERE arbre.s_id={}".format(
        stations)
    df = pd.read_sql(query, connexion)
    displot = ff.create_distplot(
        [df[c] for c in df.columns], df.columns, bin_size=.25)
    return displot


'''def fonct_1(station):
    query = "SELECT arbre.VH, recolte.Ntot, FROM arbre JOIN recolte ON arbre.id_a=recolte.a_id WHERE arbre.s_id={}".format(station)
    df = pd.read_sql(query, connexion)
    df_agreg = df.groupby(['VH']).mean()
	d = df_agreg.to_dict()['Ntot']'''


@app.callback(
    Output(component_id='aaaa', component_property='figure'),
    [Input(component_id='checklist', component_property='value')]
)
def update_graph(selected_station):
    dff = df_station[df_station['Station'].isin(selected_station)]

    return build_graph(selected_station)


if __name__ == '__main__':
    app.run_server(debug=True)
