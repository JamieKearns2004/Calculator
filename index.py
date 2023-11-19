basic_complicated = input("Would you like to do basic or complicated maths?: ")

if basic_complicated == 'basic' or basic_complicated == 'b':
    print('Would you like to do')
    input()
    print('Addition')
    print('Subtraction')
    print('Multiplication')
    print('Division')

    type_of_equation = input('Please choose one: ').lower()

    if type_of_equation == 'addition' or type_of_equation == 'add':
        number1 = float(input('What is the first number?: '))
        number2 = float(input('What is the second number?: '))
        addition_answer = number1 + number2
        print('ANSWER:', addition_answer)
        input()

    elif type_of_equation == 'subtraaction' or type_of_equation == 'sub' or type_of_equation == 'minus':
        number1 = float(input('What is the first number?: '))
        number2 = float(input('What is the second number?: '))
        if number1 > number2:
            subtraction_answer = number1 - number2
        else: 
            subtraction_answer = number2 - number1

        print('ANSWER:', subtraction_answer)
        input()

    elif type_of_equation == 'division' or type_of_equation == 'divide':
        number1 = float(input('What is the first number?: '))
        number2 = float(input('What is the second number?: '))
        division_answer = number1 / number2
        print('ANSWER:', division_answer)
        input()
    
    elif type_of_equation == 'multiplication' or type_of_equation == 'multiply':
        number1 = float(input('What is the first number?: '))
        number2 = float(input('What is the second number?: '))
        multiplication_answer = number1 * number2
        print('ANSWER:', multiplication_answer)
        input()
    
    else:
        print('Invalid option.')
        input()
else:
    print('Differenciation')
    print('Integeration')

    complication_equation_type = input('What would you like to do?: ').lower()

    if complication_equation_type == 'differenciation' or complication_equation_type == 'd':
        function_wx = input('What is the function you would like to differnciate in terms of x: ')
        input()
        if 'x' in function_wx:
            wheres_x = function_wx.index('x')
            power = int(function_wx[wheres_x + 2:])
            coefficient = int(function_wx[0:wheres_x])
            coefficient = coefficient * power
            power -= 1
            print(str(coefficient) + str('x^') + str(power))
            input()
            
    elif complication_equation_type == 'integration' or complication_equation_type == 'i':
        function_wx = input('What is the function you would like to integrate in terms of x: ')
        input()
        if 'x' in function_wx:
            wheres_x = function_wx.index('x')
            power = int(function_wx[wheres_x + 2:])
            coefficient = int(function_wx[0:wheres_x])
            coefficient = coefficient / power
            coefficient = round((coefficient), 2)
            power += 1
            print(str(coefficient) + str('x^') + str(power))
            input()
    else:
        print('test')