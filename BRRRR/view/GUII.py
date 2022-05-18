from turtle import position
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import numpy as np
import pandas as pd


from dash import dcc
from dash import dash_table


def build_dropdown_menu(menu_items):
    return dcc.Dropdown(
        id="dropdown",
        options=[{"label": x, "value": x} for x in menu_items],
        value=menu_items[:],
        multi=True,
        style={'height': '30px', 'width': '1000px'},

    )


def build_radioItems():
    return dcc.RadioItems(
        id="dropdown2",
        options=[{"label": x, "value": x} for x in ["Ntot", "oneacorn"]],
        value="Ntot",
    )


def init_scatter():
    return dcc.Graph(id="scatter")


def build_scatter(df):
    fig = px.scatter(df, x="VH", y="Ntot", color="nom",
                     marginal_x="histogram", marginal_y="rug")

    return fig


def init_sunburst():
    return dcc.Graph(id="heatmap")


def build_Heatmap(df):
    fig = go.Figure(data=go.Heatmap(
        z=df.Ntot,
        x=df.Year,
        y=df.nom,
        hoverongaps=False)
    )
    fig.update_layout(
        autosize=False,
        width=500,
        height=500)
    return fig


def build_Heatmap2(df):
    fig = go.Figure(data=go.Heatmap(
        z=df.oneacorn,
        x=df.Year,
        y=df.nom,
        # texttemplate="%{df.oneacorn}",
        hoverongaps=False))
    return fig


'''def init_displot():
    return dcc.Graph(id="displot")


def build_Distplot(df):
    dfl_Ntot = df.Ntot.tolist()
    while 'NA' in dfl_Ntot:
        dfl_Ntot.remove('NA')
    fig = ff.create_distplot([dfl_Ntot], pd.unique(df.nom).tolist(),
                             bin_size=.2, show_rug=False)
    return fig'''
