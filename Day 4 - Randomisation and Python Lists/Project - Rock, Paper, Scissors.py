import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

# 0 rock
# 1 Paper
# 2 Scissors

games = [rock, paper, scissors]
bot = random.randint(0, 2)
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors "))

if player > 2:
    print("You Lose")
else:
    print(games[player])
    print("Computer choice")
    print(games[bot])
    if bot == player:
        print('It\'s a Draw')
    elif bot == 0:
        if player == 1:
            print("Player Win. Bot Lose")
        elif player == 2:
            print("Bot Win. Player los")
    elif bot == 1:
        if player == 0:
            print("Bot Win. Player Lose")
        elif player == 2:
            print("Player Win. Bot los")
    elif bot == 2:
        if player == 0:
            print("Player Win. Bot Lose")
        elif player == 1:
            print("Bot Win. Player los")
