import pandas as pd
import sqlite3


connexion = sqlite3.connect('table_repro.db')
cursor = connexion.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     name TEXT,
     age INTERGER
)
""")
connexion.commit()
cursor = connexion.cursor()

with open('Repro_IS.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        query = 'SELECT (id) INTO station WHERE nom = "{}"'.format(
            row['Station'])
        result = cursor.execute(query)
        if result.fetchone() == None:
