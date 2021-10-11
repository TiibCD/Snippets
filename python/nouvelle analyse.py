import os
import shutil

type_analyse = input("EDD (0) / WS (1) : ")
nom_client = input("Nom client : ")
nom_fichier = nom_client + '.txt'
dossier_courant = os.getcwd()
dossier_test = 'c:/test'
analyse_modele_EDD = dossier_courant + '/_Analyse.txt'
analyse_modele_WS = dossier_courant + '/WS/_Support WS.txt'

# Analyse EDD
# On crée le dossier client qui contiendra les fichiers fournis par le client
if type_analyse == '0':
    try:
        os.mkdir(dossier_courant + '/fichiers des clients/' + nom_client)
    except OSError as error:
        print(error)
# On crée un fichier d'analyse pour le client en partant du fichier modèle
    fichier_new = dossier_courant + '/notes/' + nom_fichier
    shutil.copy(analyse_modele_EDD, fichier_new)

# On crée le dossier contenant les fichiers de test de l'interface du client
# Ajouter une possibilité de désactiver ca ?
    try:
        os.mkdir(dossier_test + '/' + nom_client)
    except OSError as error:
        print(error)

# Analyse WS
else:
    fichier_new = dossier_courant + '/WS/' + nom_fichier
    shutil.copy(analyse_modele_WS, fichier_new)


# TODO On ouvre le fichier généré dans vs code
