import random

from characters import Creature, Wizard, Small_Animal, Dragon


def main():
    print_header()
    game_loop()


def print_header():
    print('--------------------------------')
    print('      WIZARD BATTLE APP   ')
    print('--------------------------------')
    print()


def game_loop():
    creatures = [
        Small_Animal('Toad', 1),
        Creature('Tiger', 25),
        Small_Animal('Bat', 12),
        Dragon('Dragon', 50, 75, True),
        Wizard('Evil Wizard', 100),
        Dragon('Baby Dragon', 30, 20, False)
    ]

    main_character = Wizard('Gandolf', 75)

    while True:

        active_creature = random.choice(creatures)
        print(f"A {active_creature.name} of {active_creature.level} has appeared from a dark  gloomy forest")
        print(f'{main_character.name}: Level {main_character.level}')

        command = input('Do you want to [a]ttack, [r]unaway, or [l]ookaround? ')
        command = command.lower().strip()
        
        if command == 'a':
            if main_character.attack(active_creature):
                creatures.remove(active_creature)
                main_character.level += active_creature.level
            else:
                print(f'{main_character.name} has to take some time to recover')
                main_character.recovery(active_creature)
                print(f'The wizard {main_character.name} has RECOVERED to full strength')
        elif command == 'r':
            main_character.runaway()
        elif command == 'l':
            print(f'The Wizard {main_character.name} takes a look around and sees: ')
            for creature in creatures:
                print(f' * A {creature.name} of level {creature.level}')
        else:
            break

    if not creatures:
        print(f"{main_character.name} has claimed VICTORY")


if __name__ == '__main__':
    main()
