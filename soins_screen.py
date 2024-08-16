# soins_screen.py

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from soin import Soin

class SoinsScreen(Screen):
    def __init__(self, name, animaux):
        super(SoinsScreen, self).__init__(name=name)
        self.animaux = animaux

        self.layout = BoxLayout(orientation='vertical')

        # Bouton pour revenir au menu principal
        button_back = Button(text='Retour au Menu')
        button_back.bind(on_press=self.retour_menu)
        self.layout.add_widget(button_back)

        label = Label(text="Gestion des Soins")
        self.layout.add_widget(label)

        self.animal_spinner = Spinner(
            text='Sélectionner un animal',
            values=[str(animal) for animal in self.animaux]
        )
        self.layout.add_widget(self.animal_spinner)

        self.soin_type_input = TextInput(hint_text='Type de soin (Vaccination, Reproduction, Maladie, Traitement)')
        self.layout.add_widget(self.soin_type_input)

        self.details_input = TextInput(hint_text='Détails du soin')
        self.layout.add_widget(self.details_input)
        
        button = Button(text='Ajouter Soin')
        button.bind(on_press=self.ajouter_soin)
        self.layout.add_widget(button)

        self.scroll_view = ScrollView(size_hint=(1, None), size=(400, 200))
        self.scroll_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        self.scroll_layout.bind(minimum_height=self.scroll_layout.setter('height'))
        self.scroll_view.add_widget(self.scroll_layout)
        
        self.layout.add_widget(self.scroll_view)
        
        self.add_widget(self.layout)

    def ajouter_soin(self, instance):
        soin_type = self.soin_type_input.text
        details = self.details_input.text
        selected_animal_str = self.animal_spinner.text
        selected_animal = next((animal for animal in self.animaux if str(animal) == selected_animal_str), None)

        if soin_type and details and selected_animal:
            soin = Soin(soin_type, details)
            selected_animal.ajouter_soin(soin)
            self.scroll_layout.add_widget(Label(text=f"{selected_animal.race}: {soin}", size_hint_y=None, height=40))
            self.soin_type_input.text = ""
            self.details_input.text = ""
            self.animal_spinner.text = 'Sélectionner un animal'

    def retour_menu(self, instance):
        # Cette méthode permet de revenir au menu principal
        self.manager.current = 'menu'
