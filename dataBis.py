import sqlite3
import csv

# CRUD : create, read, update, delete

connexion = sqlite3.connect('table_repro_IS.db')
cursor = connexion.cursor()

with open(r'Repro_IS.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        req_station = 'SELECT * FROM t_Station WHERE nom = "{}"'.format(
            row['Station'])  # requete pour rechercher la station
        req_arbre = 'SELECT * FROM t_arbre WHERE code_arbre = "{}"'.format(
            row['code'])  # requete pour rechercher l'arbre

        res_station = cursor.execute(req_station)  # recherche de la station
        res_arbre = cursor.execute(req_arbre)  # recherche de l'arbre

        if res_station.fetchone() == None:  # if the station doesn't exist
            new_station = (row['Station'], row['Range'],
                           row['Altitude'])  # create a new station
            cursor.execute(
                'INSERT INTO t_Station VALUES (?,?,?)', new_station)  # insert the new station

        elif res_arbre.fetchone() == None:  # if the arbre doesn't exist
            new_arbre = (row['code'], row['VH'], row['H'],
                         row['SH'])  # create a new arbre
            cursor.execute(
                'INSERT INTO t_arbre VALUES (?,?,?,?)', new_arbre)  # insert the new arbre

        connexion.commit()  # commit the changes


connexion.close()  # close the connection
