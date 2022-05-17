from cgitb import text
from tkinter import CENTER
from turtle import position, right
import plotly.express as px

from dash import dcc
from dash import dash_table


# Dropdown Menu
'''def build_dropdown_menu(menu_items):
    return dcc.Dropdown(
        id="dropdown",
        options=[{"label": x, "value": x} for x in menu_items],
        value=menu_items[0],
        clearable=False
    )'''


# Range Slider
'''def build_range_slider(year):
    return dcc.RangeSlider(id='range_slider',
                           min=2011,
                           max=2020,
                           dots=True,
                           value=[2011, 2020],
                           marks={str(yr): str(yr)
                                  for yr in range(2011, 2021, 1)},
                           )'''

# Sunburst:


def init_sunburst():
    return dcc.Graph(id="sunburst")


def build_sunburst(df, attributes=[]):
    x, y = 'VH', 'Ntot'
    # df.loc[df[x] < 1000, z] = 'Other...'  # Represent only large countries
    fig = px.sunburst(df, path=[x, y], values=x,
                      color=y, hover_data=[x], title="Quantité 'Ntot' en fonction de la masse moyenne 'oneacorn'(g) dans l'intervalle du slider en année")
    return fig
