# liste_animaux_screen.py

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button

class ListeAnimauxScreen(Screen):
    def __init__(self, name, animaux):
        super().__init__(name=name)
        self.animaux = animaux

        print(self.animaux)
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
            self.scroll_layout.add_widget(Label(text=str(animal), size_hint_y=None, height=40))

    def retour_menu(self, instance):
        # Cette méthode permet de revenir au menu principal
        self.manager.current = 'menu'
