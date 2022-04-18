import sqlite3
import csv
# CRUD : create, read, update, delete

connexion = sqlite3.connect('table_repro_IS.db')
cursor = connexion.cursor()

my_code = ("213",)
cursor.execute(' SELECT * FROM t_arbre WHERE code_arbre = ? ', my_code)

print(cursor.fetchone())

connexion.close()
