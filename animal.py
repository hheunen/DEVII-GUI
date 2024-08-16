# animal.py

from soin import Soin

class Animal:
    def __init__(self, pseudo, type, race, age, regime, etat_sante):
        self.nom = pseudo # Moyen de l'identifier
        self.type = type
        self.race = race
        self.age = age
        self.regime = regime # Herbivore, omnivore ou carnivore
        self.etat_sante = etat_sante
        self.soins = []  # Liste des soins associés à cet animal

    def ajouter_soin(self, soin: Soin):
        self.soins.append(soin)
        print(self.soins[0].type_soin)

    def __str__(self):
        return f"Nom: {self.pseudo}, Type: {self.type}, Race: {self.race}, Âge: {self.age}, Régime: {self.regime}, État de santé: {self.etat_sante}"
    
    @property
    def pseudo(self):
        return self.nom
    
    @pseudo.setter
    def pseudo(self, new_nom):
        self.nom = new_nom
