# animal_screen.py

from kivy.uix.screenmanager import Screen
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from animal import Animal

class AnimalScreen(Screen):
    
    type_liste = ["Bovin","Porc","Ovin","Caprin","Vollaile"]
    
    def __init__(self, name, animaux):
        super().__init__(name=name)
        self.animaux = animaux

        layout = BoxLayout(orientation='vertical')

        # Bouton pour revenir au menu principal
        button_back = Button(text='Retour au Menu')
        button_back.bind(on_press=self.retour_menu)
        layout.add_widget(button_back)

        label = Label(text="Ajouter un Animal")
        layout.add_widget(label)
        
        # Le pseudo de l'animal
        self.pseudo_input = TextInput(hint_text='Nom/Pseudo')
        layout.add_widget(self.pseudo_input)
        
        #La listes des types d'animals
        dropdown = DropDown()
        for i in AnimalScreen.type_liste: # Pour créer chaque sélection
            btn = Button(text=i, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)
        
        self.type_input = Button(text='Sélectionnez une option', size_hint=(None, None), size=(1000, 50))
        self.type_input.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(self.type_input, 'text', x))
        layout.add_widget(self.type_input)

        #KLa race de l'animal
        self.race_input = TextInput(hint_text='Race')
        layout.add_widget(self.race_input)
        
        #L'âge de l'animal
        self.age_input = TextInput(hint_text='Âge')
        layout.add_widget(self.age_input)
        
        #Régime
        self.regime_input = TextInput(hint_text='Régime alimentaire')
        layout.add_widget(self.regime_input)
        
        #état de santé de l'animal
        self.etat_input = TextInput(hint_text='État de santé')
        layout.add_widget(self.etat_input)
        
        button = Button(text='Ajouter Animal')
        button.bind(on_press=self.ajouter_animal)
        layout.add_widget(button)

        self.scroll_view = ScrollView(size_hint=(1, None), size=(400, 200))
        self.scroll_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        self.scroll_layout.bind(minimum_height=self.scroll_layout.setter('height'))
        self.scroll_view.add_widget(self.scroll_layout)
        
        layout.add_widget(self.scroll_view)
        
        self.add_widget(layout)

    def ajouter_animal(self, instance):
        pseudo = self.pseudo_input.text
        type_a = self.type_input.text
        race = self.race_input.text
        age = self.age_input.text
        regime = self.regime_input.text
        etat = self.etat_input.text
        if pseudo and type_a and race and age and regime and etat:
            animal = Animal(pseudo, type_a,race, age, regime, etat)
            self.animaux.append(animal)
            self.scroll_layout.add_widget(Label(text=str(animal), size_hint_y=None, height=40))
            self.pseudo_input.text = ""
            self.type_input.text = "Choisir un type d\'animal"
            self.race_input.text = ""
            self.age_input.text = ""
            self.regime_input.text = ""
            self.etat_input.text = ""

    def retour_menu(self, instance):
        # Cette méthode permet de revenir au menu principal
        self.manager.current = 'menu'
