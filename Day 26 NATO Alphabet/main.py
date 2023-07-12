
import pandas as pd
nato = pd.read_csv('nato_phonetic_alphabet.csv')
my_dict = nato.set_index('letter')['code'].to_dict()
word=input("Enter a word: ").upper()
nato_list=[my_dict[letter] for letter in word]
print(nato_list)