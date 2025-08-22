import csv

def lire_objets_csv(chemin_fichier, delimiter=',', quotechar='"', has_header=True):
    """
    Générateur qui lit un fichier CSV et renvoie chaque ligne.
    - Si has_header=True, renvoie des dicts {colonne: valeur}
    - Sinon, renvoie des listes de valeurs.
    """
    with open(chemin_fichier, 'r', encoding='utf-8', newline='') as fichier:
        if has_header:
            lecteur = csv.DictReader(fichier, delimiter=delimiter, quotechar=quotechar)
        else:
            lecteur = csv.reader(fichier, delimiter=delimiter, quotechar=quotechar)
        for ligne in lecteur:
            yield ligne
