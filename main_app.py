# main_app.py

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from menu_screen import MenuScreen
from animal_screen import AnimalScreen
from liste_animaux_screen import ListeAnimauxScreen
from soins_screen import SoinsScreen
from rapport_screen import RapportScreen

class MainApp(App):
    def build(self):
        sm = ScreenManager()

        self.animaux = []

        # Ajout des écrans au ScreenManager
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(AnimalScreen(name='animal', animaux=self.animaux))
        sm.add_widget(ListeAnimauxScreen(name='liste_animaux', animaux=self.animaux))
        sm.add_widget(SoinsScreen(name='soins', animaux=self.animaux))
        sm.add_widget(RapportScreen(name='rapport', animaux=self.animaux))

        sm.current = 'menu'  # Démarrer sur l'écran du menu principal

        return sm

if __name__ == '__main__':
    MainApp().run()
