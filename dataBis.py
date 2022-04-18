import sqlite3
import csv
# CRUD : create, read, update, delete

connexion = sqlite3.connect('Vid1.db')
cursor = connexion.cursor()

my_code = ("213",)
cursor.execute(' SELECT * FROM t_arbre WHERE code_arbre = ? ', my_code)

print(cursor.fetchone())

connexion.close()
