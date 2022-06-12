import nltk as nl
from jaro import jaro_winkler_metric
class TexteDeLoi(object):

    def __init__(self, titre, date, type, collection, volume, increment, texte=[]):
        self.titre = titre
        self.date = date
        self.type = type
        self.texte = texte
        self.similarite = []
        self.collection = collection
        self.volume = volume
        self.increment = increment
        self.id = self.define_id()

    def __str__(self):
        s = self.print_low()
        s += "texte: "
        for t in self.texte:
            s += "{0}".format(t)
        return s

    def print_low(self):
        s = "___\ntitre: {f.titre}\ndate: {f.date}\ntype: {f.type}\n id: {f.id}\n volume: {f.volume}\n".format(f=self)
        return s

    def define_id(self):
        return self.collection + str("_") + str(self.volume) + str("_") + str(self.date) + str("_") + str(
            self.increment)

    def compare_jaccard(self, autreLoi):
        texte1 = set(self.texte.split())
        texte2 = set(autreLoi.texte.split())
        if len(texte2) > 10:
            value_jaccard = nl.jaccard_distance(texte1, texte2)
            if value_jaccard < 0.6:
                print(texte1)
                print(texte2)
                return value_jaccard

    def compare_levenshtein(self, autreLoi):
        return nl.edit_distance(self.texte, autreLoi.texte)

    def compare_jarowinkler(self, autreLoi):
        return jaro_winkler_metric(self, autreLoi)
