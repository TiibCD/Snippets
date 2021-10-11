import os
import shutil

nom_client = input("Nom client : ")
nom_fichier = nom_client + '.txt'
dossier_courant = os.getcwd()
dossier_test = 'c:/test'
fichier_modele = dossier_courant + '/_Analyse.txt'

# On crée le dossier client qui contiendra les fichiers fournis par le client
try:
	os.mkdir(dossier_courant + '/fichiers des clients/' + nom_client)
except OSError as error:
	print(error)

# On crée un fichier d'analyse pour le client en partant du fichier modèle
fichier_new = dossier_courant + '/notes/' + nom_fichier
shutil.copy(fichier_modele, fichier_new)

# On crée le dossier contenant les fichiers de test de l'interface du client
# Ajouter une possibilité de désactiver ca ?
try:
    os.mkdir(dossier_test + '/' + nom_client)
except OSError as error:
    print(error)

# TODO On ouvre le fichier généré dans vs code
