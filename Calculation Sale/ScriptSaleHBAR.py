
# Package import
import json
from requests import Session


# Retrieves the value of the crypto
def valueFunction():
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

# Fetch user's amount of crypto
def base():
    quantity = False
    while not quantity:
        try:
            coins = float(input("Combien avez-vous de HBAR : "))
            if coins > 0:
                quantity = True
                return coins
        except ValueError:
            print("Merci d'indiquez le chiffre valide !")
            print("")

# Recover the amount invested and calculation
def calculation():
    test = False
    while not test:
        try:
            spent = float(input("Combien avez-vous dépensé : "))
            if spent > 0:
                test = True
                coin = float(base())
                cout = float(valueFunction())
                print("HBAR est à :", float(valueFunction()),)
                gain = float(coin * cout)
                print("--------------------")
                print("")
                print("Si vous revendez, vous aurez :", round(gain, 2), "€")
                print("")
                print("Comptez une somme de :", round(gain - spent, 2), "€")
                print("")
                print("--------------------")
        except ValueError:
            print("Merci d'indiquez le chiffre valide !")
            print("")

# Start of the program
print("")
calculation()
print("Fin du programme !")
