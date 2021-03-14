
w = int(input("Insert Wight "))
h = float(input("Insert Hight 75"))

bmi = w/(h*h)

if bmi < 18.5:
        print('Your BMI is', bmi,'which means you are underweight.')
    
elif bmi <= 18.5 and bmi < 25:
        print('Your BMI is', bmi,'which means you are normal.')

elif bmi <= 25 and bmi < 30:
        print('Your BMI is', bmi,'which means you are overweight.')

elif bmi >= 30 and bmi < 35:
        print('Your BMI is', bmi,'which means you are obese.')

elif bmi > 35:
        print('Your BMI is', bmi,'which means you are Exteremely obese.')
