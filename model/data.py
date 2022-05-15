import sqlite3
import csv
# CRUD : create, read, update, delete

connexion = sqlite3.connect('table_repro_IS_test.db')
cursor = connexion.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS station (
id_s INTEGER PRIMARY KEY AUTOINCREMENT, 
nom TEXT NOT NULL, 
range INT NOT NULL,
altitude INT NOT NULL
);
''')


with open(r'Repro_IS.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')

    def STATIONFUN(chosenrow1):
        req_station = 'SELECT * FROM station WHERE nom = "{}"'.format(
            chosenrow1['Station'])

        res_station = cursor.execute(req_station)

        if res_station.fetchone() is None:
            new_station = (chosenrow1['Station'],
                           chosenrow1['Range'], chosenrow1['Altitude'])
            cursor.execute(
                'INSERT INTO station (nom, range, altitude) VALUES (?,?,?)', new_station)  # insert the new station

    for row in reader:
        STATIONFUN(row)
    connexion.commit()  # commit the changes

connexion.close()
