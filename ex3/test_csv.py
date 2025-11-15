from csv_reader import (
    charger_csv,
    FichierIntrouvableException,
    LigneInvalideException,
    PrixNegatifException
)
import os

def create_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)

def test_fichier_absent():
    try:
        charger_csv("inexistant.csv")
    except FichierIntrouvableException:
        print("FichierIntrouvableException triggered as expected")
    except Exception as e:
        print("Unexpected exception:", e)

def test_csv_valide():
    filename = "ok.csv"
    create_file(filename, "1;Pomme;3.5\n2;Poire;2\n")
    try:
        data = charger_csv(filename)
        print("Valid CSV imported:", data)
    except Exception as e:
        print("Unexpected exception:", e)
    finally:
        os.remove(filename)

def test_ligne_invalide():
    filename = "bad.csv"
    create_file(filename, "1;Banane\n2;Orange;3;Extra\n")
    try:
        charger_csv(filename)
    except LigneInvalideException:
        print("LigneInvalideException triggered as expected")
    except Exception as e:
        print("Unexpected exception:", e)
    finally:
        os.remove(filename)

def test_prix_negatif():
    filename = "neg.csv"
    create_file(filename, "1;Orange;-5\n2;Poire;abc\n")
    try:
        charger_csv(filename)
    except PrixNegatifException:
        print("PrixNegatifException triggered as expected")
    except Exception as e:
        print("Unexpected exception:", e)
    finally:
        os.remove(filename)

if __name__ == "__main__":
    test_fichier_absent()
    test_csv_valide()
    test_ligne_invalide()
    test_prix_negatif()

