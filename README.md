
# Projet CMI ISI 

# Karina Roman et Younes Bouhoreira

### Base de donnée:

Nous avons commencer par créé les quatres tables (vallee, station, arbre, recolte) qui constitue notre base de donné Repro_IS.

Pour ce faire nous avons utilisé les requêtes spécifique à la création de table.

Voici un exemple ci-dessous:

![unknown](https://user-images.githubusercontent.com/99172326/169158943-f6f333e0-d029-4c02-9926-30d8ad4dae39.png)

Ensuite nous avons pour chacune des tables, completer, à l'aide d'un fonction qui rentre les colonnes naicessaire.

Pour plusieures tables nous voulions rentrer des valeurs unique comme par exemple la table 'vallee' avec la colonne 'valley'

Pour ce faire nous somme passé par une requête qui est dans notre exemple'req_vallee'qui nous permet d'évaluer si la valeur lu sur csv est déjà présente dans la table ou non.

Ensuite chacune de ces fonction sont mis dans une boucle 'for' qui permet de parcourir toutes les lignes du csv

Voici un expemple ci-dessous de ces deux etapes:

![unknown](https://user-images.githubusercontent.com/99172326/169159043-6815bdcb-3ac3-4024-8b32-bfabea4f9cc3.png)

![unknown](https://user-images.githubusercontent.com/99172326/169159137-8bba415f-1335-49b4-82eb-21a6d160c8ac.png)

![unknown](https://user-images.githubusercontent.com/99172326/169159366-1d54f270-1851-4be4-bfa6-60f848ee25c0.png)

Une fois ces étapes temriner nous nous retrouvons avec un base de données qui nous utiliserons par la suite.

# dashapp

Nous avons réalisé quatre réprensentation. La première étant un heatmap qui montre sous forme d'intensité de couleur la quantité totale de gland produit(Ntot) ou la masse moyenne d'un gland(oneacorn) selon la seléction par station sélectionées, par année. 


La deuxième est un scatter qui montre la quantité totale de gland produit(Ntot) par station sélectioné, par rapport au volume du houppier(VH) de chaque arbre.


La troisième est un pie chart qui permet de voir la quantité totale de gland produit(Ntot) par station sélectioné.

Et la dernière est un gapminder qui montre la quantité totale de gland produit(Ntot) par station par années.


Les deux première dépendent d'un dropdown contenant les stations et de deux boutons permetant de faire un choix entre Ntot ou oneacrom

![unknown](https://user-images.githubusercontent.com/99172326/169162826-56d19694-a1f5-4b8b-836c-643fb11384ce.png)

![unknown](https://user-images.githubusercontent.com/99172326/169162086-8497ca0a-163c-48a3-a7db-22402dc90009.png)

Nous avons essayer de relier les visualisation de telle sort à ce qu'en cliquant sur une années du scatter, cela selectionne aussi la même années sur le heatmap grave au callback 'ClickData'. (Les affichages prennent un peu de temps)

![unknown](https://user-images.githubusercontent.com/99172326/169162927-4adeb75a-2d25-4ac7-9b79-0d3a9d9329fd.png)

Les deux dernières dépendent aussi d'un dropdown contenant les stations.

Nous avons essayer de crée un onglet tables et insertion permetant respectivement d'afficher nos tables et de rajouter des mesures aux tables de notre base de données.

