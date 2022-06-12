'''Formatage des XML'''

import os
from xml_parser import clean_string
from lxml import etree as ET
import re

xslt_file = ("../sources/XSLT_cleaning_Baudouin_XML_tags.xsl")

def ajout_idno(path):
#idée : trouver l'idno, lui donner le nom du fichier volume, et ensuite filtrer avec une regex
    tree = ET.parse(path)
    for node in tree.xpath("//seriesStmt[1]/idno"):
        node.text = str(path)
        node.text = str(re.sub("\D", "", str(node.text)))
        print(node.text)
        tree.write(path)


def formatage_loi(path, save_path):
     for filename in os.listdir(path):
         #parse et enlève les espaces en trop
         volume_parse = ET.parse(path + filename)
         #ajoute le numero de volume dans la deuxième balise idno
         ajout_idno(path + filename)
         clean_string(filename)
         xslt = ET.parse(xslt_file)
         transform = ET.XSLT(xslt)
         Baudouin_format = transform(volume_parse)
         #nous donne le bon texte avec le xslt appliqué
         volume_formate = ET.tostring(Baudouin_format, pretty_print=True, encoding="utf-8")
         print(filename)
         decode= volume_formate.decode()
         with open (os.path.join(save_path, filename + '_formatee.xml'), 'w', encoding='utf-8') as volume:
             volume.write(decode)


if __name__ == "__main__":
    '''il faut réitérer deux fois le code car on a un problème sinon pour "idno" : le parsage ne fonctionne pas pour le 
    placer dans le formater car il n'existe pas encore dans le volume. En exécutant deux fois d'affilée '''
    Louvre_a_formater = "../data/Louvre/"
    Louvre_save_path = "../data/Louvre_formatee/"

    formatage_loi(Louvre_a_formater, Louvre_save_path)
    formatage_loi(Louvre_a_formater, Louvre_save_path)

    Baudouin_a_formater = "../data/Baudouin/"
    Baudouin_save_path = "../data/Baudouin_formatee/"

    formatage_loi(Baudouin_a_formater, Baudouin_save_path)
    formatage_loi(Baudouin_a_formater, Baudouin_save_path)

