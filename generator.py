#!/usr/bin/env python3

from decimal import Decimal as d
import decimal
# Generator used to create my_first_calculator

# Open a file that we can write to
python_file = open('my_first_calculator.py', 'w')
# The minimum and maximum numbers we can use
min_num = -99
max_num = 99
nums = range(min_num, max_num+1)
signs = ['+', '-', '/', '*']
num_of_ifs = len(signs)*(max_num-min_num+1)**2

print(f"""#!/usr/bin/env python3

# my_first_calculator.py by AceLewis
# TODO: Make it work for all floating point numbers too

if 3/2 == 1:  # Because Python 2 does not know maths
    input = raw_input  # Python 2 compatibility

print('Welcome to this calculator!')
print('It can add, subtract, multiply and divide whole numbers from {min_num} to {max_num}')
num1 = int(input('Please choose your first number: '))
sign = input('What do you want to do? +, -, /, or *: ')
num2 = int(input('Please choose your second number: '))
print()
if num1 > {max_num} or num1 < {min_num} or num2 > {max_num} or num2 < {min_num}:
    print("Please enter only positive numbers smaller than 100 and make sure you have chosen the correct sign!")
else:""", file=python_file)

# For all the numbers and all the signs
current_sign = signs[0]
for sign in signs:
    for num1 in nums:
        for num2 in nums:
            equation = f"d({num1}){sign}d({num2})"
            try:
                equals = eval(equation)
            except ZeroDivisionError:
                equals = 'Inf'
            except decimal.InvalidOperation as error:
                if error == decimal.DivisionByZero:
                    equals = 'Inf'
                else:
                    equals = 'Undefined'
            if num2 == min_num:
                print(f"    if num1 == {num1} and sign == '{sign}' and num2 == {num2}:", file=python_file)
                print(f'        print("{num1}{sign}{num2} = {equals}")', file=python_file)
            else:
                print(f"    elif num1 == {num1} and sign == '{sign}' and num2 == {num2}:", file=python_file)
                print(f'        print("{num1}{sign}{num2} = {equals}")', file=python_file)
print('', file=python_file)
print('print("\\nThanks for using this calculator, goodbye :)")', file=python_file)

# Close the file we have written to
python_file.close()
