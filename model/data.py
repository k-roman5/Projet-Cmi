import sqlite3
import csv

# CRUD : create, read, update, delete

connexion = sqlite3.connect('table_repro_IS.db')
cursor = connexion.cursor()

with open(r'Repro_IS.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        req_station = 'SELECT * FROM t_Station WHERE nom = "{}"'.format(
            row['Station'])
        req_arbre = 'SELECT * FROM t_arbre WHERE code_arbre = "{}"'.format(
            row['code'])

        res_station = cursor.execute(req_station)
        res_arbre = cursor.execute(req_arbre)

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


connexion.close()