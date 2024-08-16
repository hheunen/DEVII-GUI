from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class ListeAnimauxScreen(Screen):
    def __init__(self, name, animaux):
        super().__init__(name=name)
        self.animaux = animaux

        layout = BoxLayout(orientation='vertical')

        # Bouton pour revenir au menu principal
        button_back = Button(text='Retour au Menu')
        button_back.bind(on_press=self.retour_menu)
        layout.add_widget(button_back)

        self.scroll_view = ScrollView(size_hint=(1, None), size=(400, 400))
        self.scroll_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        self.scroll_layout.bind(minimum_height=self.scroll_layout.setter('height'))
        self.scroll_view.add_widget(self.scroll_layout)

        layout.add_widget(self.scroll_view)
        
        self.add_widget(layout)

    def on_pre_enter(self):
        self.scroll_layout.clear_widgets()
        for animal in self.animaux:
            # Créer un bouton pour chaque animal
            btn = Button(text=str(animal), size_hint_y=None, height=40)
            # Lier le bouton à la méthode d'affichage des soins
            btn.bind(on_press=lambda instance, a=animal: self.afficher_soins(a))
            self.scroll_layout.add_widget(btn)

    def afficher_soins(self, animal):
        """Affiche la liste des soins pour l'animal sélectionné dans une fenêtre pop-up."""
        # Créer la mise en page pour la pop-up
        content = BoxLayout(orientation='vertical')
        soins = animal.soins
        
        if soins:
            for soin in soins:
                content.add_widget(Label(text=str(soin), size_hint_y=None, height=40))
        else:
            content.add_widget(Label(text="Aucun soin disponible", size_hint_y=None, height=40))

        # Bouton pour fermer la pop-up
        button_close = Button(text='Fermer', size_hint_y=None, height=40)
        button_close.bind(on_press=lambda instance: popup.dismiss())
        content.add_widget(button_close)

        # Créer et afficher la pop-up
        popup = Popup(title=f"Soins de {animal.pseudo}", content=content, size_hint=(0.8, 0.8))
        popup.open()

    def retour_menu(self, instance):
        # Cette méthode permet de revenir au menu principal
        self.manager.current = 'menu'
