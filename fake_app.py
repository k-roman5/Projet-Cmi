from ctypes import alignment

from xarray import align
import fake_GUI
import fake_data

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
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Karina Roman", className="display-4"),
        html.Hr(),
        html.P(
            u"Forêt Pyrénnées", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Sunburst", href="/sunburst", active="exact"),
            ],
            vertical=True,
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

    # Sunburst:
    if pathname == "/sunburst":

        '''dropdown = fake_GUI.build_dropdown_menu(
            fake_data.get_unique_values())'''
        '''range_slider = fake_GUI.build_range_slider(
            fake_data.get_unique_values())'''

        sunburst = fake_GUI.init_sunburst()

        return [
            html.Div([
                html.H3("Représentation Sunburst de la quantité totale de glands produits par rapport à la masse moyenne d'un gland (g)",
                        style={"margin-bottom": "0px", 'color': 'black'}),
                html.H3(),
                html.H5('Pour la période 2011-2020 pour les différentes vallées par rapport aux stations',
                        style={"margin-top": "0px", 'color': 'black'}),
                html.Hr(),

                dcc.Graph(id="sunburst", figure=fake_GUI.build_sunburst(
                    fake_data.extract_df1('Josbaig', [2012, 2016]))),

            ])
        ]

    # Else
    else:
        return html.Div(
            [
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognised..."),
            ]
        )


# Sunburst
@app.callback(
    Output("sunburst", "figure"),
    [Input("dropdown", "value"),
     Input("range_slider", "value")])
def update_sunburst(value_dropdown, value_range_slider):
    print('saluuut')
    sub_df, attributes = fake_data.extract_df1(
        value_dropdown, yearVar=value_range_slider)
    return fake_GUI.build_sunburst(sub_df, attributes)


if __name__ == '__main__':
    app.run_server(debug=True)
