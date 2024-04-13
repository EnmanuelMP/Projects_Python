import os
import random
from assets import words, logo, stages, characters_az, bcolors


def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_result(stage, word, msg):
    
    clear_screen()
    
    print("*" * 100)
    print(logo)
    print("*" * 100)
    print(stages["stage_" + str(stage)])
    print(word)
    print(msg)

def main():

    msg:str = ""
    stage:int = 0
    playing:bool = True
    word:str = random.choice(words).upper()
    player_guess:str = "_ " * len(word)

    
    word = "".join(f"{char} " for char in word)
    player_guess_list:list = list(player_guess)
    
    
    while playing:

        show_result(stage, player_guess, msg)

        guess = input("Guess a character: ").upper()

        
        if len(guess) != 1 or guess not in characters_az:
            msg = bcolors.FAIL + "Please choose only one character from a to z" + bcolors.ENDC
            continue
        

        if guess in player_guess_list:
            msg = bcolors.WARNING + f"You already choosed {guess}" + bcolors.ENDC
            continue

        if guess in word:
            for i, char in enumerate(word):
                if guess == char:
                    player_guess_list[i] = char
        else:
            stage += 1

            if stage == len(stages)-1:
                msg = bcolors.FAIL + "GAME OVER! YOU LOSE!" + bcolors.ENDC
                show_result(stage, player_guess, msg)
                playing = False
            else:
                msg = bcolors.FAIL + F"{guess} is not on word!" + bcolors.ENDC

            continue

        player_guess = "".join(player_guess_list)

        if player_guess == word:
            msg = bcolors.OKGREEN + "Congratulations! YOU WIN!" + bcolors.ENDC
            show_result(stage, player_guess, msg)
            playing = False
        
        else:
            msg = bcolors.OKGREEN + f"Great! {guess} is in word!" + bcolors.ENDC



if __name__ == '__main__':
    main()