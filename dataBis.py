import sqlite3
import csv

# CRUD : create, read, update, delete

connexion = sqlite3.connect('table_repro_IS.db')
cursor = connexion.cursor()

with open('Repro_IS.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        query = 'SELECT (id) INTO station WHERE nom = "{}"'.format(
            row['Station'])
        res = cursor.execute(query)
        if res.fetchone() == None:
            print(row['Station'])

connexion.close()
