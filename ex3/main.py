from csv_reader import (
    charger_csv,
    FichierIntrouvableException,
    LigneInvalideException,
    PrixNegatifException
)

def main():
    chemin = "articles.csv"  

    try:
        articles = charger_csv(chemin)
        print("Import reussi !")
        for a in articles:
            print(a)

    except FichierIntrouvableException as e:
        print(f"Erreur : {e}")

    except LigneInvalideException as e:
        print(f"Erreur dans le format du fichier : {e}")

    except PrixNegatifException as e:
        print(f"Erreur sur un prix : {e}")

    except Exception as e:
        print(f"Erreur inconnue : {e}")

if __name__ == "__main__":
    main()

