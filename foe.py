from random import randint
import colorama
from colorama import Fore

colorama.init(autoreset=True)


class foe:
    def __init__(self, game):
        self.game = game
        self.health = 50

    def attack(self):
        damage = randint(5, 15)
        self.game.player.health -= damage
        print(f"{Fore.RED}L'ennemi vous infliges {damage} points de dégats, il vous reste {self.game.player.health} points de vie")
