import model.data as data
import view.GUII as GUII

import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import Dash, html, Input, Output, callback_context


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
        return [GUII.build_dropdown_menu(data.dropdown_menu()), GUII.build_radioItems(), dcc.Graph(id="heatmap"), dcc.Graph(id="scatter", figure=GUII.build_scatter(data.extract_df2()))]


@ app.callback(
    Output("heatmap", "figure"),
    [Input("dropdown", "value"),
     Input("dropdown2", "value")]
)
def update_heatmap(imput_dropdown, imput_dropdown_2):
    if imput_dropdown_2 == "Ntot":
        return GUII.build_Heatmap(data.extract_df1(imput_dropdown))
    else:
        return GUII.build_Heatmap2(data.extract_df1(imput_dropdown))


if __name__ == '__main__':
    app.run_server(debug=True)
