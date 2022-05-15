import sqlite3
import csv
# CRUD : create, read, update, delete

connexion = sqlite3.connect('table_repro_IS.db')
cursor = connexion.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS arbre (
id INTEGER PRIMARY KEY AUTOINCREMENT, 
code TEXT NOT NULL,
VH REAL,
H REAL,
SH REAL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS station (
id INTEGER PRIMARY KEY AUTOINCREMENT, 
nom TEXT NOT NULL, 
range INT NOT NULL,
altitude INT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS vallee (
id INTEGER PRIMARY KEY AUTOINCREMENT, 
valley TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS recolte (
id INTEGER PRIMARY KEY AUTOINCREMENT, 
harv_num INT NOT NULL,
DD INT NOT NULL,
harv INT NOT NULL,
Year INT NOT NULL,
Date DATE NOT NULL,
Ntot1 INT NOT NULL,
Ntot INT NOT NULL,
Mtot REAL,
oneacorn REAL,
tot_Germ REAL,
M_Germ REAL,
N_Germ REAL,
rate_Germ REAL
);
''')


def VELLEYFUN(chosenrow3):
    req_vallee = 'SELECT * FROM vallee WHERE valley = "{}"'.format(
        chosenrow3['Valley'])  # requete pour rechercher la vallee
    res_vallee = cursor.execute(req_vallee)  # recherche de la vallee

    if res_vallee.fetchone() == None:  # if the valley doesn't exist
        # create a new vallee
        new_vallee = (chosenrow3['ID'], chosenrow3['Valley'])
        cursor.execute('INSERT INTO vallee VALUES (?,?)',
                       new_vallee)  # insert the new valley


with open(r'Repro_IS.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        VELLEYFUN(row)
    connexion.commit()  # commit the changes

connexion.close()
