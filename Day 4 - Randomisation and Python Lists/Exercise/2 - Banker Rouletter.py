import random

names_input = input("Give me everybody's name, seperated by comma.\n")
names = names_input.split(sep=",")

name_choice = random.choice(names)
print(f'{name_choice} is going to buy the meal today')
