from datetime import datetime
import xml.etree.ElementTree as et
from TexteDeLoi import TexteDeLoi
import os


def clean_string(texte):
    if texte:
        texte = texte.replace("\n", " ")
        texte = texte.replace("\t", " ")
        " ".join(texte.split())
        while '  ' in texte:
            texte = texte.replace('  ',' ')
        return texte

def parse_Loi(path, collection):

    tree = et.parse(path)
    lois = tree.getroot()

    # parse header - <teiHeader> = metadata
    volume = []
    for no_volume in lois.iter("idno"):  #prend le 2e idno, de respStmt et pas de publicationStmt
        numero = str(no_volume.text)
        volume = numero

    # parse text - <text> = arretés

    list_lois = []
    increment = 1

    for loi in lois.iter('div1'):

        titre = ''
        date = ''
        type = ''
        texte = ''

        if loi:

            # type (in attrib)
            type = loi.attrib.get("type")

            # titre
            titre_xml = loi.find("head")
            if titre_xml is not None:
                titre = clean_string(titre_xml.text)

            else:
                # pas de titre = pas de loi
                continue

            # date and text in paragraphs

            for item in loi.iter():
                if item.tag == "date":
                    date_string = item.get("when")
                    date_format_jj_mm_aaaa = (datetime.strptime(date_string, "%d-%m-%Y"))
                    date = date_format_jj_mm_aaaa.strftime("%Y-%m-%d")

                if item.tag == "p":
                    texte += str(clean_string(item.text)) + ' '

            if collection == "Louvre":
                collection = "L"
            if collection == "Baudouin":
                collection = "B"

            volume = volume

            loi = TexteDeLoi(titre, date, type, collection, volume, increment, texte)
            increment += 1
            list_lois.append(loi)

    return list_lois






if __name__ == "__main__":

    
    directory_name = "../data/Baudouin_formatee/"
    directory = os.listdir(directory_name)
    liste_volumes_Baudouin = []
    for file in directory:
        print(file)
        list = parse_Loi(directory_name + file, "Baudouin")
        for texte_de_loi in list:
            liste_volumes_Baudouin.extend(list)
    #
    directory_name = "../data/Louvre_formatee/"
    directory = os.listdir(directory_name)
    liste_volumes_Louvre = []
    # #
    for file in directory:
        print(file)
        list = parse_Loi(directory_name + file, "Louvre")
        for texte_de_loi in list:
            liste_volumes_Louvre.extend(list)

    dictionary_jaccard = dict()
    for texte_de_loi_Baudouin in liste_volumes_Baudouin:
        liste_distances_jaccard = []
        if texte_de_loi_Baudouin.type == "decret":
            '''Problème : on n'affiche là que les decrets, mais sur le vol1 de Baudouin, bcp d'arretés par exemple. A
            voir aussi là dessus si il n'y a pas un problème '''
            key = {texte_de_loi_Baudouin.id : ' '}
            dictionary_jaccard.update(key)
            print(texte_de_loi_Baudouin.id)
            print(dictionary_jaccard[texte_de_loi_Baudouin.id])

            for texte_de_loi_Louvre in liste_volumes_Louvre:
                if texte_de_loi_Louvre.type == "loi":
                    value = texte_de_loi_Baudouin.compare_jaccard(texte_de_loi_Louvre)
                    if value:
                        key_secondaire = texte_de_loi_Baudouin.id
                        couple = {texte_de_loi_Louvre.id : {value}}
                        dictionary_jaccard.update(couple)
                        value = texte_de_loi_Louvre.compare_jarowinkler(texte_de_loi_Baudouin)
                        print(str(texte_de_loi_Louvre.id))
                        print(str(value))
                        print(liste_distances_jaccard)
                        print(dictionary_jaccard)
