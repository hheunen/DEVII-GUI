import os
os.environ["KIVY_NO_ARGS"] = "1"

import argparse
from main_app import MainApp

def parse_args():
    parser = argparse.ArgumentParser(
        description="Application de gestion des animaux et soins",
        usage="%(prog)s [-h] -L"
    )

    # Ajout de l'argument -L pour lancer l'application
    parser.add_argument('-L', '--launch', action='store_true', help="Lancer l'application")

    args = parser.parse_args()

    if not args.launch:
        parser.print_help()
        exit(1)
    
    return args

if __name__ == '__main__':
    args = parse_args()

    if args.launch:
        MainApp().run()
