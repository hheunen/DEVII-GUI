# animal_screen.py

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from animal import Animal

class AnimalScreen(Screen):
    def __init__(self, name, animaux):
        super(AnimalScreen, self).__init__(name=name)
        self.animaux = animaux

        layout = BoxLayout(orientation='vertical')

        # Bouton pour revenir au menu principal
        button_back = Button(text='Retour au Menu')
        button_back.bind(on_press=self.retour_menu)
        layout.add_widget(button_back)

        label = Label(text="Ajouter un Animal")
        layout.add_widget(label)
        
        self.race_input = TextInput(hint_text='Race')
        layout.add_widget(self.race_input)
        
        self.age_input = TextInput(hint_text='Âge')
        layout.add_widget(self.age_input)
        
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
        race = self.race_input.text
        age = self.age_input.text
        etat = self.etat_input.text
        if race and age and etat:
            animal = Animal(race, age, etat)
            self.animaux.append(animal)
            self.scroll_layout.add_widget(Label(text=str(animal), size_hint_y=None, height=40))
            self.race_input.text = ""
            self.age_input.text = ""
            self.etat_input.text = ""

    def retour_menu(self, instance):
        # Cette méthode permet de revenir au menu principal
        self.manager.current = 'menu'
