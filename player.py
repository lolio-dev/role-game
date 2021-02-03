from random import randint
import colorama
from colorama import Fore

colorama.init(autoreset=True)


class player:
    def __init__(self, game):
        self.game = game
        self.health = 50
        self.nb_potion = 3

    def heal(self):
        nb_heal = randint(15, 50)
        self.health += nb_heal
        self.nb_potion -= 1
        print(f"{Fore.CYAN}Vous utilisez une potion qui vous redonne {nb_heal} points de vie. Il vous reste {self.nb_potion} potions")

    def attack(self):
        damage = randint(5, 10)
        self.game.foe.health -= damage
        print(f"{Fore.GREEN}Vous infligez {damage} points de dégâts à votre ennemi, il lui reste {self.game.foe.health} points de vie")
