import operator
from docx import Document
# import subprocess


# def sort_table(tableau, col):
#    return sorted(tableau, key=operator.itemgetter(col))


document = Document()

records = (
    #('Notion', 'Position', 'Titre', 'Longueur'),
    ('données perso', '3', 'Nom', '24'),
    ('données perso', '2', 'Prénom', '24'),
    ('données perso', '1', 'Matricule', '13'),
    ('données perso', '0', 'Civilité', '4'),
)

records = sorted(records, key=lambda entry: entry[1])
# records = sort_table(records, 1)


tableau = document.add_table(rows=1, cols=4)
hdr_cells = tableau.rows[0].cells
hdr_cells[0].text = 'Notion'
hdr_cells[1].text = 'Position'
hdr_cells[2].text = 'Titre'
hdr_cells[3].text = 'Longueur'


for notion, position, titre, longueur in records:
    if position != '0':
        row_cells = tableau.add_row().cells
        row_cells[0].text = notion
        row_cells[1].text = position
        row_cells[2].text = titre
        row_cells[3].text = longueur

document.save('test.docx')
