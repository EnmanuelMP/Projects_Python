import random
import subprocess
# Characters from A-Z (upper and lower cases)
characters_az = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# List of numbers 0-9
numbers_0_to_9 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# List of special characters
special_characters = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

def create_password():
    
    password:list = []

    [password.append(random.choice(characters_az)) for _ in range(random.randint(8, 10))]
    [password.append(random.choice(numbers_0_to_9)) for _ in range(random.randint(2, 4))]
    [password.append(random.choice(special_characters)) for _ in range(random.randint(2, 4))]

    random.shuffle(password)

    pwd:str = "".join(password)

    subprocess.run('echo ' + pwd.strip() + '| clip', shell=True)
    
    return pwd