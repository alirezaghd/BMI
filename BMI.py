
w =int(input("Insert Wight"))
h = int(input("Insert Hight"))

bmi = w/(h*h)

    if bmi <= 25 and < 30:
        print('Your BMI is', bmi,'which means you are overweight.')

    elif bmi => 30 and bmi < 25:
        print('Your BMI is', bmi,'which means you are obese.')


    elif bmi > 35:
        print('Your BMI is', bmi,'which means you are Exteremely obese.')
