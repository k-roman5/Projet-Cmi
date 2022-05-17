import pandas as pd
import sqlite3

# Sunburst
'''def extract_df1(value, yearVar=[]):
    df_year = df
    if yearVar != []:
        df_year = df[(yearVar[0] <= df['Year']) & (df['Year'] <= yearVar[1])]
    mask = df_year[select_column] == value
    df_valley = df_year[mask]
    # attributes used to specify grouping (and view)
    x_att = 'Ntot'
    y_att = 'oneacorn'
    z_att = 'Station'
    m_att = 'Valley'

    df_agreg = df_valley[[x_att, y_att, z_att, m_att]
                         ].groupby(by=[x_att, z_att, m_att]).sum()
    df_agreg = df_agreg.reset_index()
    return df_agreg, (x_att, y_att, z_att, m_att)'''

connexion = sqlite3.connect('table_repro_IS.db', check_same_thread=False)
df_station = pd.read_sql_query(
    '''SELECT * FROM station''', connexion)


'''def get_unique_values():
    return df_station'''


def extract_df1(stations, yearVar=[]):
    query = "SELECT arbre.VH, recolte.Ntot FROM arbre JOIN recolte ON arbre.id_a=recolte.a_id JOIN station ON station.id_s=arbre.s_id WHERE station.nom='{}'".format(
        stations)
    df = pd.read_sql(query, connexion)
    print(df)
    '''df_agreg = df.groupby(['VH']).mean()
    d = df_agreg.to_dict()['Ntot']
    df_agreg = df_agreg.reset_index()'''
# type -fonction pour type
    return df
