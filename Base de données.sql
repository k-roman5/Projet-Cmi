CREATE TABLE IF NOT EXISTS arbre (
id INTEGER PRIMARY KEY AUTOINCREMENT, 
code TEXT NOT NULL,
VH REAL,
H REAL,
SH REAL
);

CREATE TABLE IF NOT EXISTS station (
id INTEGER PRIMARY KEY AUTOINCREMENT, 
nom TEXT NOT NULL, 
range INT NOT NULL,
altitude INT NOT NULL
);

CREATE TABLE IF NOT EXISTS vallee (
id INTEGER PRIMARY KEY AUTOINCREMENT, 
valley TEXT NOT NULL
);

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


CREATE TABLE IF NOT EXISTS arbre_station ( 
id INTEGER PRIMARY KEY AUTOINCREMENT, 
arbre_id INT NOT NULL,
station_id INT NOT NULL,
FOREIGN KEY (arbre_id) REFERENCES arbre (id),
FOREIGN KEY (station_id) REFERENCES station (id) 
);

CREATE TABLE IF NOT EXISTS arbre_recolte (
id INTEGER PRIMARY KEY AUTOINCREMENT,
arbre_id INT NOT NULL,
recolte_id INT NOT NULL,
FOREIGN KEY (arbre_id) REFERENCES arbre (id),
FOREIGN KEY (recolte_id) REFERENCES recolte (id)
);

CREATE TABLE IF NOT EXISTS station_vallee (
id INTEGER PRIMARY KEY AUTOINCREMENT,
station_id INT NOT NULL,
vallee_id INT NOT NULL,
FOREIGN KEY (station_id) REFERENCES station (id),
FOREIGN KEY (vallee_id) REFERENCES vallee (id)
);

`DROP TABLE <nom de la table>;`

SELECT arbre.id, arbre.code, arbre_station.arbre_id, arbre_station.station_id, station.nom
    FROM arbre INNER JOIN arbre_station ON arbre.id=arbre_station.arbre_id
        INNER JOIN station ON arbre_station.station_id=station.id;


SELECT arbre.id, arbre.code, arbre_station.arbre_id, arbre_station.station_id, station.nom
    FROM arbre INNER JOIN arbre_station ON arbre.id=arbre_station.arbre_id
        INNER JOIN station ON arbre_station.station_id=station.id;


SELECT arbre.id, arbre.code, arbre_station.arbre_id, arbre_station.station_id, station.nom
    FROM arbre INNER JOIN arbre_station ON arbre.id=arbre_station.arbre_id
        INNER JOIN station ON arbre_station.station_id=station.id;