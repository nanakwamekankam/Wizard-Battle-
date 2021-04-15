import random
import time


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return f"Creature: {self.name} [Level: {self.level}]"

    def get_roll(self):
        return random.randint(1, 6)*self.level


class Wizard(Creature):

    def attack(self, creature):
        print(f'The wizard {self.name} attacks the {creature.name}')

        roll = self.get_roll()
        creature_roll = creature.get_roll()

        print(f"{self.name} rolls {roll}")
        print(f'{creature.name} rolls {creature_roll}')

        if roll >= creature_roll:
            print("{} has handily defeated the {}".format(self.name, creature.name))
            return True
        else:
            print(f"{self.name} has been DEFEATED")
            return False

    def recovery(self, creature):
        roll = self.get_roll()
        creature_roll = creature.get_roll()

        difference = roll - creature_roll

        return time.sleep(-difference/self.level)


    def runaway(self):
        print(f'{self.name} is unsure of his power and decides to flee...')


class Small_Animal(Creature):
    def get_roll(self):
        base_roll = super().get_roll()
        return base_roll/self.level


class Dragon(Creature):
    def __init__(self, name, level, scaliness, fire_breath):
        super().__init__(name, level)
        self.scaliness = scaliness
        self.fire_breath = fire_breath

    def get_roll(self):
        base_roll = super().get_roll()
        fire = 5 if self.fire_breath else 1
        scales = self.scaliness/10
        return (base_roll*fire*scales)/3
