age = input("What is your current age? ")

days = (90 - int(age)) * 365
weeks = (90 - int(age)) * 52
month = (90 - int(age)) * 12

print(f"You have {days} days, {weeks} weeks, {month} months left")
