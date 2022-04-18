import sqlite3
import csv

# CRUD : create, read, update, delete

connexion = sqlite3.connect('table_repro_IS.db')
cursor = connexion.cursor()

with open(r'Repro_IS.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:  # new line in csv
        print("new line")
        req_station = 'SELECT * FROM t_Station WHERE nom = "{}"'.format(
            row['Station'])  # requete pour rechercher la station

        res_station = cursor.execute(req_station)  # recherche de la station

        if res_station.fetchone() == None:  # if the station doesn't exist
            print('La station {} n\'existe pas'.format(row['Station']))
            new_station = (row['Station'], row['Range'],
                           row['Altitude'])  # create a new station
            print('station crée')
            cursor.execute(
                'INSERT INTO t_Station VALUES (?,?,?)', new_station)  # insert the new station
            print("station insérée")
        else:
            print("station existante")

        connexion.commit()  # commit the changes

with open(r'Repro_IS.csv') as csvfile_aled:
    reader_aled = csv.DictReader(csvfile_aled, delimiter=';')
    for row in reader_aled:  # new line in csv
        req_arbre = 'SELECT * FROM t_arbre WHERE code_arbre = "{}"'.format(
            row['code'])  # requete pour rechercher l'arbre
        res_arbre = cursor.execute(req_arbre)  # recherche de l'arbre

        if res_arbre.fetchone() == None:  # if the arbre doesn't exist
            print("l'arbre {} n'existe pas".format(row['code']))
            new_arbre = (row['code'], row['VH'], row['H'],
                         row['SH'])  # create a new arbre
            if row['VH'] != None:  # if the arbre has a VH
                cursor.execute(
                    'INSERT INTO t_arbre VALUES (?,?,?,?)', new_arbre)  # insert the new arbre
                print("arbre insérée")
    connexion.commit()  # commit the changes


connexion.close()  # close the connection
