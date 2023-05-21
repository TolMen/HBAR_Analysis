
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


def base():
    quantite = False
    while not quantite:
        try:
            coins = float(input("Combien avez-vous de HBAR : "))
            if coins > 0:
                quantite = True
                return coins
        except ValueError:
            print("Merci d'indiquez le chiffre valide !")
            print("")


def calcul():
    test = False
    while not test:
        try:
            depense = float(input("Combien avez-vous dépensé : "))
            if depense > 0:
                test = True
                coin = float(base())
                cout = float(valeur())
                print("HBAR est à :", float(valeur()),)
                gain = float(coin * cout)
                print("--------------------")
                print("")
                print("Si vous revendez, vous aurez :", round(gain, 2), "€")
                print("")
                print("Comptez une somme de :", round(gain - depense, 2), "€")
                print("")
                print("--------------------")
        except ValueError:
            print("Merci d'indiquez le chiffre valide !")
            print("")


print("")
calcul()
print("Fin du programme !")

# Résumé
#
# 19/02/2023 = 578.28332586 HBAR à 0.08473355 HBAR pour 50 € investis
# 22/02/2023 = 385.64512703 HBAR à 0.07623589 HBAR pour 30 € investis
#
# Total HBAR = 963.92845289


