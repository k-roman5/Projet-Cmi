import model.data
import view.GUI

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
        html.H2("CMI ISI", className="display-4"),
        html.Hr(),
        html.P(
            u"Forêt Pyrénnées", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Histogramme", href="/", active="exact"),
                dbc.NavLink("Tableur", href="/table", active="exact"),
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
    if pathname == "/":
        dropdown = view.GUI.build_dropdown_menu(model.data.get_unique_values())
        graph = view.GUI.init_graph()
        return [
            html.Div([

                dropdown, graph
            ])
        ]

    elif pathname == "/table":
        # fetch client info
        return [
            html.H1('Données forêt pyrénnées (tableur)', id='table_view',
                    style={'textAlign': 'left'}),
            html.Hr(style={'width': '75%', 'align': 'center'}),
            html.Div(id='data_table', children=view.GUI.data_table(model.data.df))
        ]

    else:
        return html.Div(
            [
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognised..."),
            ]
        )


@app.callback(
    Output("bar-chart", "figure"),
    [Input("dropdown", "value")])
def update_bar_chart(value):
    sub_df, attributes = model.data.extract_df(value)
    return view.GUI.build_figure(sub_df, attributes)


if __name__ == '__main__':
    app.run_server(debug=True)
