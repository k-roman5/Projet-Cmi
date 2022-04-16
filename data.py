import pandas as pd
import sqlite3

connexion = sqlite3.connect('table_repro.db')
cursor = connexion.cursor()
with open('Repro_IS.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
    query = 'SELECT (id) INTO station WHERE'
        nom = "{}"'.format(row['Station']) result=cursor.execute(query)
if result.fetchone() == None:
