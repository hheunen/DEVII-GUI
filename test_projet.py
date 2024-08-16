import unittest
from animal import Animal
from soin import Soin
from liste_animaux_screen import ListeAnimauxScreen
from kivy.uix.screenmanager import ScreenManager

class TestAnimal(unittest.TestCase):
    
    def setUp(self):
        """Prépare les données pour les tests."""
        self.animal = Animal(
            pseudo="Buddy",
            type="Chien",
            race="Labrador",
            age=5,
            regime="Omnivore",
            etat_sante="Bon"
        )

    def test_animal_creation(self):
        """Test la création d'un animal."""
        self.assertEqual(self.animal.pseudo, "Buddy")
        self.assertEqual(self.animal.type, "Chien")
        self.assertEqual(self.animal.race, "Labrador")
        self.assertEqual(self.animal.age, 5)
        self.assertEqual(self.animal.regime, "Omnivore")
        self.assertEqual(self.animal.etat_sante, "Bon")
        self.assertEqual(self.animal.soins, [])

    def test_ajouter_soin(self):
        """Test l'ajout d'un soin à un animal."""
        soin = Soin("Vaccination", "Vacciné contre la rage")
        self.animal.ajouter_soin(soin)
        self.assertEqual(len(self.animal.soins), 1)
        self.assertEqual(self.animal.soins[0].type_soin, "Vaccination")
        self.assertEqual(self.animal.soins[0].details, "Vacciné contre la rage")
        self.assertEqual(str(self.animal), "Nom: Buddy, Type: Chien, Race: Labrador, Âge: 5, Régime: Omnivore, État de santé: Bon")

class TestSoin(unittest.TestCase):
    
    def setUp(self):
        """Prépare les données pour les tests."""
        self.soin = Soin("Vaccination", "Vacciné contre la rage")

    def test_soin_creation(self):
        """Test la création d'un soin."""
        self.assertEqual(self.soin.type_soin, "Vaccination")
        self.assertEqual(self.soin.details, "Vacciné contre la rage")
        self.assertEqual(str(self.soin), "Type du soin = Vaccination, Détails = Vacciné contre la rage")

class TestListeAnimauxScreen(unittest.TestCase):
    
    def setUp(self):
        """Prépare les données pour les tests."""
        self.animaux = [
            Animal(
                pseudo="Buddy",
                type="Chien",
                race="Labrador",
                age=5,
                regime="Omnivore",
                etat_sante="Bon"
            ),
            Animal(
                pseudo="Mittens",
                type="Chat",
                race="Siamois",
                age=3,
                regime="Carnivore",
                etat_sante="Excellent"
            ),
        ]
        self.screen_manager = ScreenManager()
        self.screen = ListeAnimauxScreen(name="animaux_list", animaux=self.animaux)
        self.screen_manager.add_widget(self.screen)

    def test_liste_animaux_screen(self):
        """Test l'affichage des animaux dans l'écran de liste d'animaux."""
        self.screen.on_pre_enter()

        # Vérifier le nombre d'éléments ajoutés à la liste
        self.assertEqual(len(self.screen.scroll_layout.children), len(self.animaux))

        # Les enfants sont ajoutés dans l'ordre inverse dans Kivy, donc vérifiez l'ordre correct
        self.assertEqual(self.screen.scroll_layout.children[-1].text, "Nom: Buddy, Type: Chien, Race: Labrador, Âge: 5, Régime: Omnivore, État de santé: Bon")
        self.assertEqual(self.screen.scroll_layout.children[-2].text, "Nom: Mittens, Type: Chat, Race: Siamois, Âge: 3, Régime: Carnivore, État de santé: Excellent")

if __name__ == "__main__":
    unittest.main()
