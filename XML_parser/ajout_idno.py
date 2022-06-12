import os
from xml_parser import clean_string
from lxml import etree as ET
import re

def ajout_idno(path):
#idée : trouver l'idno, lui donner le nom du fichier volume, et ensuite filtrer avec une regex
    tree = ET.parse(path)
    for node in tree.xpath("//seriesStmt[1]/idno"):
        node.text = str(path)
        node.text = str(re.sub("\D", "", str(node.text)))
        print(node.text)

if __name__ == "__main__":
    
    Baudouin_format = ("../data/Baudouin")
    Baudouin_formatee = os.listdir(Baudouin_format)
    for file in Baudouin_formatee:
        ajout_idno(f"../data/Baudouin/{file}")

