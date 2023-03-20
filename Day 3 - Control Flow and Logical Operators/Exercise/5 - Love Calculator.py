name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

name = name1+" "+name2
t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")
true = t + r+ u + e

l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")
love = l + o + v + e

score = int(str(true)+str(love))
msg = ""
if score in range(40, 50):
    msg = f"Your score is {score}, you are alright together."
elif score < 10 or score > 90:
    msg = f"Your score is {score}, you are alright together."
else:
    msg = f"Your score is {score}."

print(msg)


