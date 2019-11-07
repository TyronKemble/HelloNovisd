"""Naam: Tyron Kemble

Leerlijn: Python
Datum: 22 juli
"""


import random
import pickle

from ChatApplicatieNovi import UserKlasse


class RegistratieKlasse(UserKlasse.User):

    def __init__(self, id, name,email):
        UserKlasse.User.__init__(self, id,name ,email)

    def Registratie():
        Naam = input("Naam van de nieuwe gebruiker: ")

        Email = input("Email adress: ")

        try:
            f = open("NieuweGebruiker.txt", "w")
        except:
            print("Kan het bestand  NieuweGebruiker.txt voor de registratie niet aanmaken")

        def RandomNumber():
            n = 0
            for x in range(10):
                for x in range(10):
                    n = random.randint(1, 101)
            return n

        try:
            with open("NieuweGebruiker.txt", 'wb') as f:
                pickle.dump(Naam, f)
        except:
            print("Kan het bestand NieuweGebruiker.txt voor de registratie niet weg schrijven")

        print("Welkom " +Naam+ " Kies optie 1 om met jou gebruikernaam in te loggen")

        return  RegistratieKlasse(RandomNumber(),Naam,Email)





