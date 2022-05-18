import model.data
import view.GUI


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

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])

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

image_filename = 'black_oak.png'  # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

sidebar = html.Div(
    [dbc.NavLink(html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode())), href="/",
                 active="exact"),
        html.H2("Forêt Pyrénnées", className="display-4",),

        dbc.Nav(
            [
                dbc.NavLink("Accueil", href="/",
                            active="exact"),
                dbc.NavLink("Visualisations", href="/visualisations",
                            active="exact"),
                dbc.NavLink("Tableur", href="/table",
                            active="exact"),
                dbc.NavLink("Insertion", href="/insertion",
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

    elif pathname == "/visualisations":
        #dropdown = view.GUI.build_dropdown_menu(model.data.get_unique_values())
        #graph = view.GUI.init_graph()
        return [
            html.Div([

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

    elif pathname == "/insertion":
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


if __name__ == '__main__':
    app.run_server(debug=True)
