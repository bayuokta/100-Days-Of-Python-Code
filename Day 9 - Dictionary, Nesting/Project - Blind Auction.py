logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print('Welcome to the secret auction program')
bidders = True
data = {}
value = 0
winner = ""

while bidders:
    name = input('What is your name?: ').lower()
    bid = int(input('What\'s your bid?:$ '))
    bidders = True if input("Are there any other bidders? 'Yes' or 'No'").lower() == 'yes' else False
    data[name] = bid


for key in data:
    if value < data[key]:
        value = data[key]
        winner = key

print(f'The winner is {winner} with a bid of ${value}')
