"""Naam: Tyron Kemble

Leerlijn: Python
Datum: 21 juli
"""
import  pickle

from  ChatApplicatieNovi import UserKlasse
from ChatApplicatieNovi import Client
from  ChatApplicatieNovi import Admin
from ChatApplicatieNovi import  RegistratieKlasse





class Permission(UserKlasse.User):

    __Niewebruiker = ''

    def __init__(self, id, naam, email):
        super().__init__(id, naam, email)

    def checkUsername(self, name):
                if name == client1.get__naam() or name == client2.get__naam() or name == admin.get__naam() or name == Permission.ReadNieuweGebruiker():
                    return True
                else:
                    return  False

    def RegisterAccountAndCheckPermission(self):

        self.__Niewebruiker = RegistratieKlasse.RegistratieKlasse.Registratie().get__naam()

        return self.__Niewebruiker

    def ReadNieuweGebruiker():
        try:
            inFile = open('NieuweGebruiker.txt', 'rb')
        except:
            print("Kan het bestand NieuweGebruiker.txt niet uitlezen ")

        newlist = pickle.load(inFile)

        fullword = ''

        for l in newlist:
            fullword += l
        return fullword


client1 = Client.Client(1, "Tyron", "TyronKemble@gmail.com")
client2 = Client.Client(12, "Melissa", "Melissa.Kemble@gmail.com")
admin = Admin.Admin(100, "Henk", "Henk.Vrieswijk@gmail.com")

