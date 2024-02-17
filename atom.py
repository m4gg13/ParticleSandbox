class Atom:
    def __init__(self):
        self.type = "atom"

class Hydrogen(Atom):
    def __init__(self, number):
        super().__init__()
        self.number = number
        self.electrons = 2
        self.protons = 2
        self.neutrons = 2
