import plotly.express as px

connexion = sqlite3.connect('table_repro_IS.db')

#df = px.data.tips()
# fig = px.histogram(df, x="total_bill", y="tip", color="sex", marginal="rug",
#                  hover_data=df.columns)
# fig.show()


def DistplotsFUN(chosenYear):

    query = "SELECT * FROM recolte WHERE {}={}".format('Year', chosenYear)
    fig = px.histogram(
        query, x=query["VH"], y=query["Ntot"], color=query["Station"], marginal="rug")
    fig.show()
