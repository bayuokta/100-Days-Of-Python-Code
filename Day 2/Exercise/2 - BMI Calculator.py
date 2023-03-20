height = input('enter your height in m: ')
weight = input('enter your weight in kg: ')

bmi = int(weight) / (float(height)/100)**2

print('BMI: '+ str(bmi))