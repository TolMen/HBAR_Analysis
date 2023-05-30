# Package import
import json
from requests import Session


# Retrieves the value of the crypto
def valeur():
    try:
        # API URL to take crypto value
        url = 'https://api3.binance.com/api/v3/ticker/price?symbol=HBARUSDT'

        # Recovery process
        collect = Session()
        login = collect.get(url)
        data = json.loads(login.text)

        # Value storage
        value = data['price']
        return value
    except:
        print("Erreur API")


# Request the amount invested
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
    # Program start

    # Crypto Value Call
    prix = float(valeur())

    print("")
    print("HBAR est à", prix, "USDT/$.")
    print("")

    # Call to the info request function
    depot = info()

    # Calculation of the number of crypto
    crypto = float(depot) / float(valeur())

    print("----------")
    print("")
    print("Vous aurez", round(crypto, 2), "HBAR.")

    # Forecast 2032
    prevision = 3.75
    gain = crypto * prevision

    print("")
    print("----------")
    print("Si HBAR atteint :", prevision, "$ en 2032.")
    print("Alors votre gain monte à :", round(gain - depot, 2), "$")
    print("")
    print("Fin du programme")


script()
