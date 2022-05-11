#import model.data
#import view.GUI


from tkinter import CENTER
from turtle import position
import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SKETCHY])

# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "width": "90rem",
    "padding": "2rem 1rem",
    "text-align": "center",
    # "background-color": "#f8f9fa",
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("CMI ISI", className="display-4"),
        html.Hr(),
        html.P(
            u"Forêt Pyrénnées", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Histogramme", href="/", active="exact"),
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

if __name__ == '__main__':
    app.run_server(debug=True)
