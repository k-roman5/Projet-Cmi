import sqlite3
import csv

# CRUD : create, read, update, delete

connexion = sqlite3.connect('table_repro_IS.db')
cursor = connexion.cursor()

with open(r'Repro_IS.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:  # new line in csv
        print("new line")
        req_station = 'SELECT * FROM t_Station WHERE nom = "{}"'.format(
            row['Station'])  # requete pour rechercher la station

        res_station = cursor.execute(req_station)  # recherche de la station

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

with open(r'Repro_IS.csv') as csvfile_aled:
    reader_aled = csv.DictReader(csvfile_aled, delimiter=';')
    for row in reader_aled:  # new line in csv
        req_arbre = 'SELECT * FROM t_arbre WHERE code_arbre = "{}"'.format(
            row['code'])  # requete pour rechercher l'arbre
        res_arbre = cursor.execute(req_arbre)  # recherche de l'arbre

        if res_arbre.fetchone() == None:  # if the arbre doesn't exist
            print("l'arbre {} n'existe pas".format(row['code']))
            new_arbre = (row['code'], row['VH'], row['H'],
                         row['SH'])  # create a new arbre
            if row['VH'] != None:  # if the arbre has a VH
                cursor.execute(
                    'INSERT INTO t_arbre VALUES (?,?,?,?)', new_arbre)  # insert the new arbre
                print("arbre insérée")
    connexion.commit()  # commit the changes

with open(r'Repro_IS.csv') as csvfile_aled:
    reader_aled = csv.DictReader(csvfile_aled, delimiter=';')
    for row in reader_aled:  # new line in csv
        req_vallee = 'SELECT * FROM t_vallee WHERE valley = "{}"'.format(
            row['Valley'])  # requete pour rechercher la vallee
        res_vallee = cursor.execute(req_vallee)  # recherche de la vallee

        if res_vallee.fetchone() == None:  # if the valley doesn't exist
            print("la vallee {} n'existe pas".format(row['Valley']))
            new_vallee = (row['Valley'])  # create a new vallee
            cursor.execute(
                'INSERT INTO t_vallee VALUES (?)', new_vallee)  # insert the new valley
            print("vallee insérée")
    connexion.commit()  # commit the changes

with open(r'Repro_IS.csv') as csvfile_aled:
    reader_aled = csv.DictReader(csvfile_aled, delimiter=';')
    for row in reader_aled:  # new line in csv
        req_recolte = 'SELECT * FROM t_recolte WHERE numero = "{}"'.format(
            row['harv_num'])  # requete pour rechercher la recolte
        res_recolte = cursor.execute(req_recolte)  # recherche de la recolte

        if res_recolte.fetchone() == None:  # if the "recolte" doesn't exist
            print("la recolte {} n'existe pas".format(row['code']))
            new_recolte = (row['harv_num'], row['DD'], row['harv'], row['Year'], row['Date'], row['Ntot1'], row['Ntot'], row['Mtot'],
                           row['oneacorn'], row['tot_Germ'], row['M_Germ'], row['N_Germ'], row['rate_Germ'])  # create a new "recolte"
            cursor.execute(
                'INSERT INTO t_recolte VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)', new_recolte)  # insert the new "recolte"
            print("recolte insérée")
    connexion.commit()  # commit the changes

connexion.close()  # close the connection
