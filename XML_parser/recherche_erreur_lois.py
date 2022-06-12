
from datetime import datetime
import xml.etree.ElementTree as et
import os

def date_loi(path):
    tree = et.parse(path)
    lois = tree.getroot()

    for loi in lois.iter('div1'):
            date = ''
            if loi:
                for item in loi.iter():
                    if item.tag == "date":
                        date_string = item.get("when")
                        date1 = (datetime.strptime(date_string, "%d-%m-%Y"))
                        date = date1.strftime("%Y-%m-%d")

path = ('../Revloi et LexDir/Collection Louvre/')

if __name__ == "__main__":
    directory_name = "../Revloi et LexDir/Collection Louvre/"
    directory = os.listdir(directory_name)
    liste_volumes_Baudouin = []
    for file in directory:
        print(file)
        list = date_loi(directory_name + file)
        print(list)
