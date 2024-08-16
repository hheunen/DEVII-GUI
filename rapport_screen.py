from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

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
        self.button_sauvegarder.bind(on_press=self.create_pdf)
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
        """Sauvegarde le rapport généré dans un fichier PDF."""
        rapport = self.rapport_label.text
        if not rapport:
            print("Aucun rapport à sauvegarder.")
            return

        # Nom du fichier PDF
        filename = "rapport_animaux.pdf"
        
        # Chemin complet (vous pouvez le personnaliser)
        filepath = os.path.join(os.getcwd(), filename)
        
        # Création du PDF
        c = canvas.Canvas(filepath, pagesize=A4)
        width, height = A4

        # Écriture du texte dans le PDF
        c.drawString(100, height - 50, "Rapport des Soins des Animaux")
        y_position = height - 80

        for line in rapport.splitlines():
            c.drawString(50, y_position, line)
            y_position -= 15  # Déplace la prochaine ligne un peu plus bas

        # Sauvegarde du fichier
        c.save()

        print(f"Rapport sauvegardé sous : {filepath}")

    def retour_menu(self, instance):
        # Cette méthode permet de revenir au menu principal
        self.manager.current = 'menu'
