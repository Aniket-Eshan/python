import math
import time

print('Calculator')

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return 'Error: Cannot divide by zero! Returning to options...'
    return a / b

def power(a, b):
    return a ** b

def root(a, b):
    if b == 0:
        return 'Error: Cannot divide by zero! Returning to options...'
    if a < 0:
        return 'Error: Cannot take square root of negative number! Returning to options...'
    return a ** (1 / b)

def calculator():
    while True:
        time.sleep(1)
        print('')
        print('--- Calculator Menu ---')
        print('1. Add')
        print('2. Subtract')
        print('3. Multiply')
        print('4. Divide')
        print('5. Power')
        print('6. Root')
        print('0. Exit')

        choice = input('Type a number from 0 to 6: ')

        if choice == '0':
            print('Are you sure you want to exit?')
            print('1. Yes')
            exit = input('0. No ')
            if exit == '1':
                break
            else:
                print('Going back...')
                time.sleep(1)

        elif choice == '1':
            a = int(input('What is the first addent? '))
            b = int(input('What is the second addent? '))
            result = addition(a, b)
            print('Result:', result)

        elif choice == '2':
            a = int(input('What is the minuend? '))
            b = int(input('What is the subtrahend? '))
            result = subtraction(a, b)
            print('Result:', result)

        elif choice == '3':
            a = int(input('What is the first factor? '))
            b = int(input('What is the second factor? '))
            result = multiplication(a, b)
            print('Result:', result)

        elif choice == '4':
            a = int(input('What is the dividend? '))
            b = int(input('What is the divisor? '))
            result = division(a, b)
            print('Result:', result)

        elif choice == '5':
            a = int(input('What is the number? '))
            b = int(input('What is the power? '))
            result = power(a, b)
            print('Result:', result)

        elif choice == '6':
            a = int(input('What is the number? '))
            b = int(input('What is the root? (e.g., 2 for square root) '))
            result = root(a, b)
            print('Result:', result)

        else:
            print('Invalid choice. Pick a number from 0 to 6.')

calculator()
