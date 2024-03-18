#TODO: Theses are the function for getting the sum, product, difference and quotient of the two numbers
def addition(x, y):
    sum = x + y
    return f'The sum of {x} + {y} is {sum}'

def multiplication(x, y):
    product = x * y
    return f'The product of {x} * {y} is {product}'

def subtraction(x, y):
    difference = x - y #Get the absolute value of the number
    return f'The difference of {x} - {y} is {difference}'

def division(x, y):
    quotient = x / y
    return f'The quotient of {x} / {y} is {quotient}'

# NOTE: This function is for problem 1 Mathematical Operators
def mathematical_operators(operator):
    print('Mathematical Operators')
    num1 = float(input('Enter Num1: ')) # NOTE: f you want to perform numerical operations on this input, you need to convert it to a numeric type (like int or float).
    num2 = float(input('Enter Num2: '))
    if operator == '1':
            print(addition(num1, num2)) 
    elif operator == '2':
            print(subtraction(num1, num2))
    elif operator == '3':
            print(multiplication(num1, num2))
    elif operator == '4':
            print(division(num1, num2))
    else:
            print('Invalid operator')

def unit_conversion(celsius):
    print('Unit Conversion')
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def get_percentage(part, whole):
    total_percentage =  (float(part) / float(whole)) * 100
    return total_percentage

def string_manipulation(input_char):
    print('String Manipulation')
    string = 'Hello, World. This is a string'
    print(f'String: {string}')
    print(f'Length: {len(string)}') #NOTE: len() is used to get the total length of the string including the spaces
    if input_char in string: #NOTE: The in Keyword si used to check if a value exist in the sequence
        return f"'{input_char}' exists in the string: '{string}'"
    else:
        return f"'{input_char}' does not exist in the string: '{string}'"

def module_two_activity(selected):
    print(selected)
    if selected == '1':
        print('Mathematical Operator')
        print('1 - Addition')
        print('2 - Subtraction')
        print('3 - Multiplication')
        print('4 - Division')

        operator = input('Enter Operator: ')
        mathematical_operators(operator)

    elif selected == '2':
        celsius = float(input('Enter Celsius: '))
        print(f'{celsius}°C is equal to {unit_conversion(celsius)}°F')

    elif selected == '3':
        char = input('Input a character: ')
        print(string_manipulation(char))
    elif selected == '4':
        part = input('Part: ')
        whole = input('Whole:')
        print(f'{part} is {get_percentage(part, whole)}% of {whole}') #NOTE: f stands for "formatted string literals. " F-strings provide a concise and convenient way to embed expressions inside string literals, allowing you to create strings with embedded variables or expressions directly within them.

print('Module 2 activity: Working with functions')
print('1 - Mathematical Operators')
print('2 - Unit Conversion')
print('3 - String Manipulation')
print('4 - Get Percentage')
user_input = input('Enter your choice: ')
module_two_activity(user_input)
