import json
# import subprocess
from docx import Document

# Ouverture du fichier json
with open('ChampsImportSalarie.json', 'r', encoding='UTF-8') as json_data:
    enregistrements = json.load(json_data)

# Tri des élements par position
enregistrements = sorted(
    enregistrements, key=lambda entry: int(entry['position']))

# TODO Pouvoir générer un fichier Excel
# Lecture du document
document = Document('TableauImport.docx')

# TODO RAZ du document word
# Création du tableau
tableau_word = document.add_table(rows=1, cols=6)
# Utilisation d'un style
tableau_word.style = document.styles['StyleTableauImport']

hdr_cells = tableau_word.rows[0].cells
hdr_cells[0].text = 'Notion'
hdr_cells[1].text = 'Position'
hdr_cells[2].text = 'Titre'
hdr_cells[3].text = 'Format'
hdr_cells[4].text = 'Exemple'
hdr_cells[5].text = 'Commentaire'

# Ecriture des élements dans le tableau (si position !=0)
for entity in enregistrements:
    if entity['position'] != '0':
        row_cells = tableau_word.add_row().cells
        row_cells[0].text = entity['notion']
        row_cells[1].text = entity['position']
        row_cells[2].text = entity['champ']
        row_cells[3].text = entity['format']
        row_cells[4].text = entity['exemple']
        row_cells[5].text = entity['commentaire']

document.save('TableauImport.docx')

# RAZ des positions dans le fichier json (si paramètre en entrée)
raz_position = input("RAZ des positions dans le fichier json ? (y/N) : ")
if raz_position == "y":
    for entity in enregistrements:
        entity['position'] = '0'
    # Ecriture du fichier json
    # TODO souci d'encoding
    with open('ChampsImportSalarie.json', 'w', encoding='UTF-8') as json_data:
        json.dump(enregistrements, json_data, indent=2)

# TODO Gérer l'ouverture du fichier généré
# subprocess.run(['open' + document], check=True)
