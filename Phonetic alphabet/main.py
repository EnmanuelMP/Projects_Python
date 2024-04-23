import pandas as pd

path="C:\\Users\\enman\\Desktop\\Projects\\Phonetic alphabet"
df = pd.read_csv(f"{path}\\nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
Phonetics = {row.letter:row.code for index, row in df.iterrows()}
print(Phonetics)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Say a word: ").upper()
Phonetic_word = [Phonetics[letter] for letter in word]
print(Phonetic_word)