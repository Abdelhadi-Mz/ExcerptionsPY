import csv
import os
class CsvException(Exception):
    def __init__(self, message):
        super().__init__(message)


class FichierIntrouvableException(CsvException): pass
class LigneInvalideException(CsvException): pass
class PrixNegatifException(CsvException): pass

def charger_csv(chemin):
    if not os.path.exists(chemin):
        raise FichierIntrouvableException(f"Fichier introuvable : {chemin}")

    articles = []

    with open(chemin, newline="", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=';')

        for ligne in reader:
            
            if not ligne or ligne == ['']:
                continue

            if len(ligne) != 3:
                raise LigneInvalideException(f"Ligne invalide : {ligne}")

            id_article, nom, prix_str = ligne

            
            try:
                prix = float(prix_str)
            except ValueError:
                raise PrixNegatifException(f"Prix non numerique : {prix_str}")

            if prix < 0:
                raise PrixNegatifException(f"Prix negatif : {prix}")

            articles.append({
                "id": id_article,
                "nom": nom,
                "prix": prix
            })

    return articles