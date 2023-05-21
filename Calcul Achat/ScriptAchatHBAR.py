# Importation paquet
import json
from requests import Session


# Récupére la valeur de la crypto
def valeur():
    try:
        # URL de l'API pour prendre la valeur de la crypto
        url = 'https://api3.binance.com/api/v3/ticker/price?symbol=HBARUSDT'

        # Processus de récupération
        collect = Session()
        login = collect.get(url)
        data = json.loads(login.text)

        # Stockage de la valeur
        value = data['price']
        return value
    except:
        print("Erreur API")


# Demande la somme investie
def info():
    mise = False
    while not mise:
        try:
            taux = float(input("Le taux de l'euro en dollar est de : "))
            somme = int(input("Combien voulez-vous investir en € : "))
            if somme > 0:
                print("J'enregistre", round(somme * taux), "$.")
                mise = True
                return somme
        except ValueError:
            print("Merci d'indiquez un nombre entier valide !")
            print("")


def script():
    # Début programme

    # Appel à la valeur de la crypto
    prix = float(valeur())

    print("")
    print("HBAR est à", prix, "USDT/$.")
    print("")

    # Appel à la fonction de demande d'info
    depot = info()

    # Calcul du nombre de crypto
    crypto = float(depot) / float(valeur())

    print("----------")
    print("")
    print("Vous aurez", round(crypto, 2), "HBAR.")

    # Prévision 2032
    prevision = 3.75
    gain = crypto * prevision

    print("")
    print("----------")
    print("Si HBAR atteint :", prevision, "$ en 2032.")
    print("Alors votre gain monte à :", round(gain - depot, 2), "$")
    print("")
    print("Fin du programme")


script()
