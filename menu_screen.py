# menu_screen.py

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MenuScreen(Screen):
    def __init__(self, name):
        super(MenuScreen, self).__init__(name=name)
        layout = BoxLayout(orientation='vertical')

        # Bouton pour aller à l'écran d'ajout d'animaux
        button_ajout_animal = Button(text='Ajouter un Animal')
        button_ajout_animal.bind(on_press=self.go_to_ajout_animal)
        layout.add_widget(button_ajout_animal)

        # Bouton pour aller à l'écran de liste des animaux
        button_liste_animaux = Button(text='Liste des Animaux')
        button_liste_animaux.bind(on_press=self.go_to_liste_animaux)
        layout.add_widget(button_liste_animaux)

        # Bouton pour aller à l'écran de gestion des soins
        button_soins = Button(text='Gestion des Soins')
        button_soins.bind(on_press=self.go_to_soins)
        layout.add_widget(button_soins)

        # Bouton pour aller à l'écran de génération de rapport
        button_rapport = Button(text='Génération de Rapport')
        button_rapport.bind(on_press=self.go_to_rapport)
        layout.add_widget(button_rapport)

        self.add_widget(layout)

    def go_to_ajout_animal(self, instance):
        self.manager.current = 'animal'

    def go_to_liste_animaux(self, instance):
        self.manager.current = 'liste_animaux'

    def go_to_soins(self, instance):
        self.manager.current = 'soins'

    def go_to_rapport(self, instance):
        self.manager.current = 'rapport'
