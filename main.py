from player import player
from foe import foe

import colorama
from colorama import Fore

colorama.init(autoreset=True)


class game:
    def __init__(self):
        self.foe = foe(self)
        self.player = player(self)

    def round(self):
        ask = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")

        if ask == "1":
            self.player.attack()
        elif ask == "2":
            if game.player.nb_potion > 0:
                self.player.heal()
            else:
                print("plus de potion")

        self.foe.attack()


game = game()
running = True

while running:
    if game.player.health > 0 and game.foe.health > 0:
        game.round()

    elif game.player.health <= 0:
        print(f"{Fore.RED}Désolé vous avez perdu")
        running = False

    elif game.foe.health <= 0:
        print(f"{Fore.GREEN}👏 bravo vous avez gagné ")
        running = False
