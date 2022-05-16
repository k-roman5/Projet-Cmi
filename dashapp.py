#import model.data
#import view.GUI


from tkinter import CENTER
from turtle import position
import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from xarray import align

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

                #dropdown, graph
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


if __name__ == '__main__':
    app.run_server(debug=True)
