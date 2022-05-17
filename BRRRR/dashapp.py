import model.data as data
import view.GUII as GUII

import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
#from matplotlib.pyplot import figure

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.PULSE])

content = html.Div(id="page-content", children=[])

app.layout = html.Div([
    dcc.Location(id="url"),
    content,
])


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return [GUII.build_dropdown_menu(data.dropdown_menu()), dcc.Graph(id="heatmap"), dcc.Graph(id="distplot", figure=GUII.build_Distplot(data.extract_df1('Gedre-Bas')))]


@ app.callback(
    Output("heatmap", "figure"),
    [Input("dropdown", "value")]
)
def update_heatmap(value):
    return GUII.build_Heatmap(data.extract_df1(value))


# def update_heatmap(value):
#    return GUII.build_Distplot(data.extract_df1(value))


if __name__ == '__main__':
    app.run_server(debug=True)
