import model.data as data
import model.data_db as data_db
import view.GUI as GUI


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
    "top": 0,
    "left": 0,
    "width": "90rem",
    "padding": "2rem 1rem",
    "text-align": "center",
    "background-color": "#f8f9fa",
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "4rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

image_filename = 'black_oak.png'  # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

sidebar = html.Div(
    [dbc.NavLink(html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()), style={'height': '80px', 'width': '80px'}), href="/",
                 active="exact", style={'height': '0px', 'width': '1000px'}),
        html.H1("Forêt Pyrénnées", className="display-4",
                style={"width": "92rem"}),

        dbc.Nav(
            [
                dbc.NavLink("Accueil", href="/",
                            active="exact"),
                dbc.NavLink("Visualisations méthode 1", href="/visualisations",
                            active="exact"),
                dbc.NavLink("Visualisations méthode 2", href="/visualisations2",
                            active="exact")
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
    if pathname == "/":
        return [
            html.Hr(),

            html.P('Projet realisé par Karina Roman et Younes Bouhoreira, etudiants en Cmi isi L2.   Mai-Avril 2022', style={
                'textAlign': 'left'}),
            html.Hr('Nous voulions remercier notre professeur Mr. MELANCON pour nous avoir accompagnées tout au long du semestre et de nous avoir aidées à la réalisation de notre projet.'),
        ]

    elif pathname == "/visualisations":
        dropdown = GUI.build_dropdown_menu(data.dropdown_menu())
        radioItems = GUI.build_radioItems()
        heatmap = dcc.Graph(id="heatmap")
        # scatter = dcc.Graph(id="scatter")
        gapminder = dcc.Graph(id="gapminder")

        return [

            dropdown, html.Hr(), radioItems, html.Hr(),
            html.Div([gapminder], style={
                'display': 'inline-block'}),

            html.Div([heatmap], style={
                'display': 'inline-block'})

        ]

    # Table
    elif pathname == "/visualisations2":
        dropdown = GUI.build_dropdown_menu(data.dropdown_menu())
        pie = dcc.Graph(id="pie")
        scatter = dcc.Graph(id="scatter")
        return [
            dropdown, html.Hr(), pie, scatter
        ]

    else:
        return html.Div(
            [
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognised..."),
            ]
        )


@ app.callback(
    Output("gapminder", "figure"),
    [Input("dropdown", "value"),
     Input("radioItems", "value")])
def update_gapminder(imput_dropdown, imput_dropdown_2):
    return GUI.build_scatter(data.extract_df1(imput_dropdown))


@ app.callback(
    Output("heatmap", "figure"),
    [Input("dropdown", "value"),
     Input("radioItems", "value")]
)
def update_heatmap(imput_dropdown, imput_dropdown_2):
    if imput_dropdown_2 == "Ntot":
        return GUI.build_Heatmap(data.extract_df1(imput_dropdown))
    else:
        return GUI.build_Heatmap2(data.extract_df1(imput_dropdown))


@ app.callback(
    Output("pie", "figure"),
    [Input("dropdown", "value")])
def update_Box_Plot(value):
    return GUI.build_pie(data.extract_df1(value))


@ app.callback(
    Output("scatter", "figure"),
    [Input("pie", "clickData")])
def update_heatmap(click):
    if click is None:
        return {}
    click = click["points"][0]["x"]
    return GUI.build_scatter(df_mask=data.extract_df3()['nom'] == 'click')


if __name__ == '__main__':
    app.run_server(debug=True)
