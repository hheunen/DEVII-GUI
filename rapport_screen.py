# rapport_screen.py

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class RapportScreen(Screen):
    def __init__(self, animaux, name):
        super(RapportScreen, self).__init__(name=name)
        self.animaux = animaux

        self.layout = BoxLayout(orientation='vertical')
        # Bouton pour revenir au menu principal
        button_back = Button(text='Retour au Menu')
        button_back.bind(on_press=self.retour_menu)
        self.layout.add_widget(button_back)

        self.label = Label(text="Génération de Rapport")
        self.layout.add_widget(self.label)
        
        self.button_generer = Button(text='Générer Rapport')
        self.button_generer.bind(on_press=self.generer_rapport)
        self.layout.add_widget(self.button_generer)

        self.rapport_label = Label(text="")
        self.layout.add_widget(self.rapport_label)

        self.button_sauvegarder = Button(text='Sauvegarder en PDF')
        self.button_sauvegarder.bind(on_press=self.sauvegarder_pdf)
        self.layout.add_widget(self.button_sauvegarder)
        
        self.add_widget(self.layout)

    def generer_rapport(self, instance):
        rapport = "Rapport généré:\n\n"
        for animal in self.animaux:
            rapport += str(animal) + "\n"
            rapport += "Soins reçus:\n"
            for soin in animal.soins:
                rapport += f"  - {soin}\n"
            rapport += "\n"
        self.rapport_label.text = rapport

    def sauvegarder_pdf(self, instance):
        # Fonctionnalité de sauvegarde à implémenter
        print("Sauvegarder en PDF: Fonctionnalité non implémentée")

    def retour_menu(self, instance):
        # Cette méthode permet de revenir au menu principal
        self.manager.current = 'menu'