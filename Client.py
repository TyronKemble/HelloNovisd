"""Naam: Tyron Kemble

Leerlijn: Python
Datum: 15 juli
"""

from ChatApplicatieNovi import  UserKlasse


class Client (UserKlasse.User):
    def __init__(self, id,naam, email):
        super().__init__(id,naam, email)

