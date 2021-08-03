import os
import shutil

nom_client = input("Nom client : ")
nom_fichier = nom_client + '.txt'
dossier_courant = os.getcwd()
fichier_modele = dossier_courant + '/_Analyse.txt'

# On crée le dossier client qui contiendra les fichiers fournis par le client
os.mkdir(dossier_courant + '/fichiers des clients/' + nom_client)

# On crée un fichier d'analyse pour le client en partant du fichier modèle
fichier_new = dossier_courant + '/notes/' + nom_fichier
shutil.copy(fichier_modele, fichier_new)

# TODO On ouvre le fichier généré dans vs code
