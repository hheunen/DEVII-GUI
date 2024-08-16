# soin.py

class Soin:
    def __init__(self, type_soin, details):
        self.type_soin = type_soin
        self.details = details

    def __str__(self):
        return f"Type: {self.type_soin}, Détails: {self.details}"
