from assets import logo, characters_az, numbers_0_to_9, special_characters, bcolors
import os
import random

def create_password(pwd_len_char:int, pwd_len_number:int, pwd__len_specialChar:int):
    password:list = []

    for _ in range(1,pwd_len_char + 1):
        password.append(random.choice(characters_az))

    for _ in range(1,pwd_len_number +1):
        password.append(random.choice(numbers_0_to_9))

    for _ in range(1,pwd__len_specialChar + 1):
        password.append(random.choice(special_characters))

    random.shuffle(password)

    pwd:str = ""

    for char in password:
        pwd += char

    print(pwd)



def main():
    clear = lambda: os.system('cls')
    print(logo)

    while True:
        
        try:
            pwd_len_char:int = int(input("How many characters would you like in your password?\n"))
            pwd_len_number:int = int(input("How many numbers would you like in your password?\n"))
            pwd__len_specialChar:int = int(input("How many special characters would you like in your password?\n"))
            break
        except:
            clear()
            print(logo)
            print(bcolors.FAIL + "Please insert a valid number not a text." + bcolors.ENDC)
    
    create_password(pwd_len_char,pwd_len_number,pwd__len_specialChar)
    

    
if __name__ == '__main__':
    main()