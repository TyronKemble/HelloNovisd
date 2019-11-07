"""Naam: Tyron Kemble

Leerlijn: Python
Datum: 15 juli
"""

from ChatApplicatieNovi import  UserKlasse


class Admin (UserKlasse.User):
    def __init__(self, id, name,email):
        super().__init__(id,name ,email)
