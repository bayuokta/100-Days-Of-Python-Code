# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def main(card):
    player = []
    bot = []
    for i in range(2):
        player.append(random.choice(card))
        bot.append(random.choice(card))
    print(f'Your card: {player}, current score: {sum(player)}')
    print(f'Computer\'s first card: {bot[0]}')
    if input("Type 'y' to get another card, type 'n' to pass: ").lower() == 'y':
        player.append(random.choice(card))
        bot.append(random.choice(card))
        print(f'Your card: {player}, current score: {sum(player)}')
        print(f'Computer\'s first card: {bot[0]}')
        if sum(player) >= 21:
            print("You went over. You lose 😭")
        if sum(bot) >= 21:
            print("Opponent went over. You win 😁")

# if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
#     pass

main(cards)
