height = input('enter your height in m: ')
weight = input('enter your weight in kg: ')

bmi = int(weight) / (float(height)/100)**2
value = ""

if bmi < 18.5:
    value = "Underweight"
elif bmi > 18.5 and bmi < 25:
    value = "normal weight"
elif bmi > 25 and bmi < 30:
    value = "slightly overweight"
elif bmi > 30 and bmi < 35:
    value = "slightly overweight"
elif bmi > 35:
    value = "clinically obese"
    

print('BMI: '+ str(int(bmi)) + " ",value)