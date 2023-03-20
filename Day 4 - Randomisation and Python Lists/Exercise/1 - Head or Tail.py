import random

rand = random.randint(0, 1)
# menggunakan ternary operator
# nilai1 if kondisi else nilai2
choice = "Head" if rand == 1 else "Tail"

print(choice)
