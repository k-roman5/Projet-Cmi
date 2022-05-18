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
        style={"margin-left": "6rem", "margin-bottom": "3rem",
               "height": "30px", "width": "900px"})


def build_radioItems():
    return dcc.RadioItems(
        id="radioItems",
        options=[{"label": x, "value": x} for x in ["Ntot", "oneacorn"]],
        value="Ntot", style={"margin": "0px" "0px" "-4px", "border-radius": "10px", "margin-left": "35rem", "border": "solid", "height": "30px", "width": "200px", "text-align": "center"
                             })


def init_scatter():
    return dcc.Graph(id="scatter")


def build_scatter(df):
    fig = px.scatter(df, x="VH", y="Ntot", color="nom",
                     marginal_x="histogram", marginal_y="rug", width=500, height=500, style={"margin": "-4px" "0px" "-4px"})
    return fig


def build_gapminder(df, val):
    fig = px.bar(df, x="Year", y=val,
                 hover_data=["Mtot", "VH"], color="nom",
                 labels={"Ntot": "Quantité totale de glands produits", "oneacorn": "Masse moyenne d'un gland (g)"}, height=400)
    return fig


def build_Heatmap(df):
    fig = go.Figure(data=go.Heatmap(
        z=df.Ntot,
        x=df.Year,
        y=df.nom,
        hoverongaps=False))
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
