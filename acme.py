
import random

class Product:
    def __init__(self, name=None, price=10, weight=20, flammability=0.5, identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        s_value = self.price / self.weight
        if s_value < 0.5:
            print("Not so stealable...")
        elif s_value >= 1:
            print("Very stealable!")
        else:
            print("Kinda stealable.")

    def explode(self):
        e_value = self.flammability * self.weight
        if e_value < 10:
            print("...fizzle.")
        elif e_value >= 50:
            print("...BABOOM!!")
        else:
            print("...boom!")


class BoxingGlove(Product):
    def __init__(self, weight):
        super().__init__(weight=10)

    def explode(self):
        print("...it's a glove.")

    def punch(self):
        weight = self.weight
        if weight < 5:
            print("That tickles.")
        elif weight >= 15:
            print("OUCH!")
        else:
            print("Hey that hurt!")
