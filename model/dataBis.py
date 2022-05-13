from asyncio.windows_events import NULL
from queue import Empty
import sqlite3
import csv

# CRUD : create, read, update, delete

connexion = sqlite3.connect('table_repro_IS.db')
cursor = connexion.cursor()

with open(r'Repro_IS.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')

    def STATIONFUN(chosenrow1):
        req_station = 'SELECT * FROM t_Station WHERE nom = "{}"'.format(
            chosenrow1['Station'])

        res_station = cursor.execute(req_station)

        if res_station.fetchone() is None:
            new_station = (chosenrow1['Station'],
                           chosenrow1['Range'], chosenrow1['Altitude'])
            cursor.execute(
                'INSERT INTO t_Station VALUES (?,?,?)', new_station)  # insert the new station

    def TREEFUN(chosenrow2):
        req_arbre = 'SELECT * FROM t_arbre WHERE code_arbre = "{}"'.format(
            chosenrow2['code'])  # requete pour rechercher l'arbre
        res_arbre = cursor.execute(req_arbre)  # recherche de l'arbre

        if res_arbre.fetchone() == None:  # if the arbre doesn't exist
            print("l'arbre {} n'existe pas".format(chosenrow2['code']))
            new_arbre = (chosenrow2['code'], chosenrow2['VH'], chosenrow2['H'],
                         chosenrow2['SH'])  # create a new arbre
            if row['VH'] != None:  # if the arbre has a VH
                cursor.execute(
                    'INSERT INTO t_arbre VALUES (?,?,?,?)', new_arbre)  # insert the new arbre
                print("arbre insérée")

    def VELLEYFUN(chosenrow3):
        req_vallee = 'SELECT * FROM t_vallee WHERE valley = "{}"'.format(
            chosenrow3['Valley'])  # requete pour rechercher la vallee
        res_vallee = cursor.execute(req_vallee)  # recherche de la vallee

        if res_vallee.fetchone() == None:  # if the valley doesn't exist
            new_vallee = (chosenrow3['Valley'])  # create a new vallee
            cursor.execute('INSERT INTO t_vallee VALUES (?)',
                           (new_vallee,))  # insert the new valley

    def RECOLTEFUN(chosenrow4):
        new_recolte = (chosenrow4['harv_num'], chosenrow4['DD'], chosenrow4['harv'], chosenrow4['Year'], chosenrow4['Date'], chosenrow4['Ntot1'], chosenrow4['Ntot'],
                       chosenrow4['Mtot'], chosenrow4['oneacorn'], chosenrow4['tot_Germ'], chosenrow4['M_Germ'], chosenrow4['N_Germ'], chosenrow4['rate_Germ'])  # create a new "recolte"
        cursor.execute(
            'INSERT INTO t_recolte VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)', new_recolte)  # insert the new "recolte"
        print("recolte insérée")

    def TREENONEFUN():
        req_arbre_none = 'DELETE FROM t_arbre WHERE VH == NULL'
        res_arbre_none = cursor.execute(req_arbre_none)

    for row in reader:
        STATIONFUN(row)
        TREEFUN(row)
       # TREENONEFUN()
        VELLEYFUN(row)
        RECOLTEFUN(row)

        connexion.commit()

    connexion.close()  # close the connection
