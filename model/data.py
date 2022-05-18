import pandas as pd
import sqlite3

connexion = sqlite3.connect('table_repro_IS.db', check_same_thread=False)


def extract_df1(stations):
    df = pd.DataFrame()
    for station in stations:
        query = "SELECT station.nom, recolte.Ntot, recolte.Year,arbre.VH, recolte.oneacorn FROM station JOIN arbre ON id_s=s_id JOIN recolte ON id_a=a_id  WHERE nom='{}'".format(
            station)
        df = pd.concat([df, pd.read_sql(query, connexion)])
    return df


def extract_df2():
    query = "SELECT station.nom, recolte.Year,recolte.Ntot,arbre.VH FROM station JOIN arbre ON id_s=s_id JOIN recolte ON id_a=a_id"
    df = pd.read_sql(query, connexion)
    return df


def dropdown_menu():
    query = "SELECT DISTINCT nom FROM station"
    df = pd.read_sql(query, connexion)
    return df.nom.tolist()
