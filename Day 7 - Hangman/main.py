import random
import hangman_art
from hangman_word import word_list

chosen_word = random.choice(list(word_list))
print(hangman_art.logo)
print(f'Pssst, the solution is {chosen_word}.')
len_word = len(chosen_word)
display = []
lives = 6
for i in range(len_word):
    display.append("_")
print(display)
while '_' in display and lives > 0:
    guest = input('Guess a letter: ').lower()

    for i in range(len_word):
        letter = chosen_word[i]
        if letter == guest:
            display[i] = guest

    if guest not in chosen_word:
        lives -= 1

    print(hangman_art.stages[lives])
    print(" ".join(display))

message = "You Win" if lives != 0 else "You Lose"
print(message)
