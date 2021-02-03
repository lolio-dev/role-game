from player import player
from foe import foe

import colorama
from colorama import Fore

colorama.init(autoreset=True)


class game:
    def __init__(self):
        self.foe = foe(self)
        self.player = player(self)
        self.running = True

    def round(self):
        ask = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")

        if ask == "1":
            self.player.attack()
        elif ask == "2":
            if game.player.nb_potion > 0:
                self.player.heal()
            else:
                print(f"{Fore.RED}plus de potion !!!")

        self.foe.attack()

    def restart(self):
        ask_restart = input("Voulez vous rejouer ? oui(o) non(n)")
        if ask_restart == "o":
            self.player.health = 50
            self.player.nb_potion = 3
            self.foe.health = 50
        elif ask_restart == 'n':
            self.running = False


game = game()

while game.running:
    if game.player.health > 0 and game.foe.health > 0:
        game.round()

    elif game.player.health <= 0:
        print(f"{Fore.RED}Désolé vous avez perdu")
        game.restart()

    elif game.foe.health <= 0:
        print(f"{Fore.GREEN}👏 bravo vous avez gagné ")
        game.restart()
