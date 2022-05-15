import sqlite3
import csv

from numpy import indices

# CRUD : create, read, update, delete

connexion = sqlite3.connect('table_repro_IS.db')
cursor = connexion.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS vallee (
id_v INTEGER PRIMARY KEY AUTOINCREMENT, 
valley TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS station (
id_s INTEGER PRIMARY KEY AUTOINCREMENT, 
nom TEXT NOT NULL, 
range INT NOT NULL,
altitude INT NOT NULL,
v_id INTEGER,
FOREIGN KEY (v_id) REFERENCES valley(id_v)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS arbre (
id_a INTEGER PRIMARY KEY AUTOINCREMENT, 
code TEXT NOT NULL,
VH REAL,
H REAL,
SH REAL,
s_id INTEGER,
FOREIGN KEY (s_id) REFERENCES station(id_s)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS recolte (
id_r INTEGER PRIMARY KEY AUTOINCREMENT, 
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
rate_Germ REAL,
a_id INTEGER,
FOREIGN KEY (a_id) REFERENCES arbre(id_a)
);
''')

with open(r'Repro_IS.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')

    def VELLEYFUN(chosenrow3):
        req_vallee = 'SELECT id_v FROM vallee WHERE valley = "{}"'.format(
            chosenrow3['Valley'])  # requete pour rechercher la vallee
        res_vallee = cursor.execute(
            req_vallee).fetchone()  # recherche de la vallee

        if res_vallee == None:  # if the valley doesn't exist
            # create a new vallee
            new_vallee = (chosenrow3['Valley'])
            cursor.execute('INSERT INTO vallee (valley) VALUES (?)',
                           [new_vallee])  # insert the new valley
            return cursor.execute('SELECT MAX(id_v) FROM vallee').fetchone()[0]
        return res_vallee[0]

    def STATIONFUN(chosenrow1, id_v):
        req_station = 'SELECT * FROM station WHERE nom = "{}"'.format(
            chosenrow1['Station'])

        res_station = cursor.execute(req_station)

        if res_station.fetchone() is None:
            new_station = (chosenrow1['Station'],
                           chosenrow1['Range'], chosenrow1['Altitude'], id_v)
            cursor.execute(
                'INSERT INTO station (nom, range, altitude, v_id) VALUES (?,?,?,?)', new_station)  # insert the new station

    def TREEFUN(chosenrow2):

        req_arbre = 'SELECT * FROM arbre WHERE code = "{}"'.format(
            chosenrow2['code'])  # requete pour rechercher l'arbre

        res_arbre = cursor.execute(req_arbre)  # recherche de l'arbre

        if res_arbre.fetchone() == None:  # if the arbre doesn't exist
            new_arbre = (chosenrow2['code'], chosenrow2['VH'], chosenrow2['H'],
                         chosenrow2['SH'])  # create a new arbre
            if row['VH'] != None:  # if the arbre has a VH
                cursor.execute(
                    'INSERT INTO arbre (code,VH,H,SH) VALUES (?,?,?,?)', new_arbre)  # insert the new arbre

    def RECOLTEFUN(chosenrow4):
        new_recolte = (chosenrow4['harv_num'], chosenrow4['DD'], chosenrow4['harv'], chosenrow4['Year'], chosenrow4['Date'], chosenrow4['Ntot1'], chosenrow4['Ntot'],
                       chosenrow4['Mtot'], chosenrow4['oneacorn'], chosenrow4['tot_Germ'], chosenrow4['M_Germ'], chosenrow4['N_Germ'], chosenrow4['rate_Germ'])  # create a new "recolte"
        cursor.execute(
            'INSERT INTO recolte (harv_num, DD, harv, Year, Date, Ntot1, Ntot, Mtot, oneacorn, tot_Germ, M_Germ, N_Germ, rate_Germ) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', new_recolte)  # insert the new "recolte"

    def TREENONEFUN():
        req_arbre_none = 'DELETE FROM arbre WHERE VH == NULL'
        res_arbre_none = cursor.execute(req_arbre_none)

    for row in reader:
        id_v = VELLEYFUN(row)
        STATIONFUN(row, id_v)
        TREEFUN(row)
        # TREENONEFUN()
        RECOLTEFUN(row)

        connexion.commit()

    connexion.close()  # close the connection
