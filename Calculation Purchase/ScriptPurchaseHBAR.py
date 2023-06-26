# Package import
import json
from requests import Session


# Retrieves the value of the crypto
def fonctionValue():
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
    bet = False
    while not bet:
        try:
            rate = float(input("Le taux de l'euro en dollar est de : "))
            sum = int(input("Combien voulez-vous investir en € : "))
            if sum > 0:
                print("J'enregistre", round(sum * rate), "$.")
                bet = True
                return sum
        except ValueError:
            print("Merci d'indiquez un nombre entier valide !")
            print("")


def script():
    # Program start

    # Crypto Value Call
    price = float(fonctionValue())

    print("")
    print("HBAR est à", price, "USDT/$.")
    print("")

    # Call to the info request function
    deposit = info()

    # Calculation of the number of crypto
    crypto = float(deposit) / float(fonctionValue())

    print("----------")
    print("")
    print("Vous aurez", round(crypto, 2), "HBAR.")

    # Forecast 2032
    forecast = 3.75
    gain = crypto * forecast

    print("")
    print("----------")
    print("Si HBAR atteint :", forecast, "$ en 2032.")
    print("Alors votre gain monte à :", round(gain - deposit, 2), "$")
    print("")
    print("Fin du programme")


script()
