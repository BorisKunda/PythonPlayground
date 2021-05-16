from typing import List


class Avenger:
    def __init__(self, name, attack):
        self.name = name + " ---- "
        self.attack = attack


# -----

print("AVENGERS ASSEMBLE !!!")

a1 = Avenger("Spiderman", "SHOOTS WEBS")
a2 = Avenger("Punisher", "LAUNCHES ROCKET")
a3 = Avenger("Thor", "THROWS HAMMER")

avengers: List[Avenger] = [a1, a2, a3]

for hero in avengers:
    print(hero.name + hero.attack)
