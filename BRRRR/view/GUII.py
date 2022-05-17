import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff

from dash import dcc
from dash import dash_table


def build_dropdown_menu(menu_items):
    return dcc.Dropdown(
        id="dropdown",
        options=[{"label": x, "value": x} for x in menu_items],
        value=menu_items[:],
        multi=True
    )


def init_distplot():
    return dcc.Graph(id="distplot")


def build_Distplot(df):
    fig = ff.create_distplot(df.Ntot, df.nom, colors=df.nom,
                             bin_size=.2, show_rug=False)


def init_sunburst():
    return dcc.Graph(id="heatmap")


def build_Heatmap(df):
    fig = go.Figure(data=go.Heatmap(
        z=df.Ntot,
        x=df.Year,
        y=df.nom,
        hoverongaps=False))
    return fig
