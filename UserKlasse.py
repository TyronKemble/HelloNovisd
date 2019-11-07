"""Naam: Tyron Kemble

Leerlijn: Python
Datum: 15 juli
"""

class User (object):
    def __init__(self,id,naam, email):
        self.__id = id
        self.__naam = naam
        self.__email = email

    def get__id(self):
        return self.__id

    def set__id(self, id):
        self.__id = id

    def get__naam(self):
        return self.__naam

    def set__naam(self, name):
        self.__naam = naam

    def get__email(self):
        return self.__email

    def set__email(self, email):
        self.__email = email
