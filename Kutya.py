import random

class Kutya:
    def __init__(self, nev, nem, faj, magassag, suly):
        self.nev = nev
        self.nem = nem
        self.faj = faj
        self.magassag = magassag
        self.suly = suly

    def get_nev(self):
        return self.nev

    def __str__(self):
        return f"{self.nev}, ({self.nem}, {self.faj}, {self.magassag}, {self.suly})"

    def tevekenyseg(self):
        
        tev = ""
        vel = int(random.random() * 3) + 1

        if vel == 1:
            tev = "ugat"
        elif vel == 2:
            tev = "alszik"
        else:
            tev = "játszik"

        harap = ""

        if vel == 1:
            harap = ", és harap"

        print(self.nev + " " + tev + harap)
        self.tev = vel



