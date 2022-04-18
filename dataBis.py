import sqlite3
import csv

# CRUD : create, read, update, delete

connexion = sqlite3.connect('table_repro_IS.db')
cursor = connexion.cursor()

with open(r'C:\Users\Younes\Downloads\Repro_IS (2).csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        print("Nouvelle ligne :")
        query = 'SELECT * FROM t_Station WHERE nom = "{}"'.format(
            row['Station'])
        res = cursor.execute(query)
        if res.fetchone() == None:  # if the station doesn't exist
            print("res.fetchone() :", res.fetchone())
            new_station = (cursor.lastrowid,
                           row['Station'], row['Range'], row['Altitude'])
            cursor.execute(
                'INSERT INTO t_Station VALUES (?,?,?,?)', new_station)
            print("Station créée")
            connexion.commit()
    connexion.commit()


connexion.close()
