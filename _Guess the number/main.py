import random, os
from assets import bcolors


def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def run():
    Number = random.randint(1,101)
    print(Number)
    
    try:
        Guess = int(input("Guess the number: "))
    except:
            clear_screen()
            print(bcolors.FAIL + "Please insert a valid number not a text." + bcolors.ENDC)

    if Guess == Number:
        print("Congratulations! you win!")

    else:
         print("Good try...")
         
if __name__ == '__main__':
    run()