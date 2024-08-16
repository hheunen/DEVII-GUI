# animal.py

from soin import Soin

class Animal:
    def __init__(self, race, age, etat_sante):
        self.race = race
        self.age = age
        self.etat_sante = etat_sante
        self.soins = []  # Liste des soins associés à cet animal

    def ajouter_soin(self, soin: Soin):
        self.soins.append(soin)

    def __str__(self):
        return f"Race: {self.race}, Âge: {self.age}, État de santé: {self.etat_sante}"
