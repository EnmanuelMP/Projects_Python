from assets import logo, results, figueres, bcolors
import random
import os

def main():
    wants_to_play = True
    clear = lambda: os.system('cls')
    print(logo)

    while wants_to_play:
        
        

        try:
            player:str = input("Enter your choice (rock, paper, or scissors): ").lower()
            NPC:str = random.choice(list(figueres.keys()))

            battle:str = f'{player}_vs_{NPC}'

            print(
                "Player Choose:",
                figueres[player],
                "NPC Choose:",
                figueres[NPC],
                "\n",
                results[battle],
                "\n",
                sep="\n"
            )
        except:
                clear()
                print(logo)
                print(bcolors.FAIL + "Please choose a valid option." + bcolors.ENDC)
                continue

        wants_to_play = True if input("Play again? Y/N: \n").lower() == "y" else False
        clear()
        print(logo)

if __name__ == "__main__":
    main()