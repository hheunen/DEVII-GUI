from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from soin import Soin

class SoinsScreen(Screen):
    def __init__(self, name, animaux):
        super().__init__(name=name)
        self.animaux = animaux
        self.the_selected_animal= None

        layout = BoxLayout(orientation='vertical')

        # Bouton pour revenir au menu principal
        button_back = Button(text='Retour au Menu')
        button_back.bind(on_press=self.retour_menu)
        layout.add_widget(button_back)

        label = Label(text="Gestion des Soins")
        layout.add_widget(label)

        # Initialisation de l'animal_spinner, le Dropdown sera configuré dans on_pre_enter
        self.animal_spinner = Button(text=f'Sélectionnez un animal', size_hint=(None, None), size=(1000, 50))
        layout.add_widget(self.animal_spinner)

        # Type de soin
        self.soin_type_input = TextInput(hint_text='Type de soin (Vaccination, Reproduction, Maladie, Traitement)')
        layout.add_widget(self.soin_type_input)

        # Details des soins
        self.details_input = TextInput(hint_text='Détails du soin')
        layout.add_widget(self.details_input)
        
        button = Button(text=f'Ajouter Soin')
        button.bind(on_press=self.ajouter_soin)
        layout.add_widget(button)

        self.scroll_view = ScrollView(size_hint=(1, None), size=(400, 200))
        self.scroll_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        self.scroll_layout.bind(minimum_height=self.scroll_layout.setter('height'))
        self.scroll_view.add_widget(self.scroll_layout)
        
        layout.add_widget(self.scroll_view)
        
        self.add_widget(layout)

    def on_pre_enter(self):
        """Cette méthode est appelée juste avant que l'écran devienne actif."""
        dropdown = DropDown()
        
        for animal in self.animaux:
            btn = Button(text=animal.pseudo, size_hint_y=None, height=44)
            # On utilise un closure pour capturer la référence correcte d'animal
            btn.bind(on_release=lambda btn, a=animal: self.select_animal(a, dropdown))
            dropdown.add_widget(btn)
        
        # Re-lier le bouton à l'ouverture du dropdown
        self.animal_spinner.bind(on_release=dropdown.open)

    def select_animal(self, animal, dropdown):
        """Cette méthode gère la sélection d'un animal depuis le dropdown."""
        self.the_selected_animal = animal
        self.animal_spinner.text = animal.pseudo
        dropdown.dismiss()

    def ajouter_soin(self, instance):
        soin_type = self.soin_type_input.text
        details = self.details_input.text
        selected_animal = self.the_selected_animal

        if soin_type and details and selected_animal:
            soin = Soin(soin_type, details)
            selected_animal.ajouter_soin(soin)
            self.scroll_layout.add_widget(Label(text=f"L'animal {selected_animal.race} a : {soin}", size_hint_y=None, height=40))
            self.soin_type_input.text = ""
            self.details_input.text = ""
            self.animal_spinner.text = 'Sélectionner un animal'
            self.the_selected_animal = None  # Réinitialiser la sélection après l'ajout


    def retour_menu(self, instance):
        # Cette méthode permet de revenir au menu principal
        print(self.animaux)
        print("-------")
        print(self.animaux[0].soins)
        self.manager.current = 'menu'
