import pandas as pd

df_nato_phonetic = pd.read_csv('nato_phonetic_alphabet.csv')

word = 'Thomas'.upper()
dict_word_nato = {value.letter: value.code for (key, value) in df_nato_phonetic.iterrows()}
list_word_nato = [dict_word_nato.get(letter) for letter in word]
print(list_word_nato)
