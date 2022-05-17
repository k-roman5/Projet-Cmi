import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate


import plotly.graph_objects as go
import plotly.express as px
import sqlite3
import pandas as pd


#df = px.data.tips()
# fig = px.histogram(df, x="total_bill", y="tip", color="sex", marginal="rug",
#                  hover_data=df.columns)
# fig.show(


# Range Slider
def build_range_slider(year):
    return dcc.RangeSlider(id='range_slider',
                           min=2011,
                           max=2020,
                           dots=True,
                           value=[2011, 2020],
                           marks={str(yr): str(yr)
                                  for yr in range(2011, 2021, 1)},
                           )


def get_stations():
    connexion = sqlite3.connect('table_repro_IS.db')
    query = "SELECT nom, id FROM station"
    cursor = connexion.cursor()
    result = cursor.execute(query)
    return result.fetchall()


'''def prepare_data(chosenYear, station_list):
    if station_list == None:
	    raise PreventUpdate
	else:
        connexion = sqlite3.connect('table_repro_IS.db')
        if len(station_list) == 1:
		    station = station_list[0]
		    query = "SELECT arbre.VH, recolte.Ntot, recolte.Year, FROM arbre JOIN recolte ON arbre.id_a=recolte.a_id WHERE arbre.s_id={}".format(station)
        else:
			query = "SELECT arbre.VH, recolte.Ntot, FROM arbre JOIN recolte ON arbre.id_a=recolte.a_id WHERE arbre.s_id IN {}".format(tuple(station_list))
    df = pd.read_sql(query, connexion)
    df_agreg = df.groupby(['VH', 'Year']).mean()
    d = df_agreg.to_dict()['Ntot']
    years = sorted(set([x[1] for x in d.keys()]))
    arbres = set([x[0] for x in d.keys()])'''


def DistplotsFUN(chosenYearMin, chosenYearMax, chosenStation):
    query = "SELECT * FROM recolte WHERE {} >= {} AND {} <= {} AND {} = {} ".format(
        'Year', chosenYearMin, 'Year', chosenYearMax, 's_id', chosenStation)
    fig = px.histogram(
        query, x=query["VH"], y=query["Ntot"], color=query["Station"], marginal="rug")
    return fig
