# Nested if/else
# Nested if/else
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
    elif age in range(12, 18):
        bill = 7
    elif age >= 45 and age <= 55:
        bill = 0
    else:
        bill = 12
    
    wants_photo = input("Do you want a photo taken? Y or N ")
    if wants_photo == "Y" or wants_photo == "y":
        bill += 3
    
    message = "Everthing is going to be ok. Have a free ride on us" if (age >= 45 and age <=50) and bill == 0 else f'Your total bill is ${bill}'
    print(message)
else:
    print("Sorry, you have to grow taller before you can ride")