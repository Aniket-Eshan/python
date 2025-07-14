import math
import statistics
import time

print('Calculator')

# Basic operations
def addition(a, b): return a + b
def subtraction(a, b): return a - b
def multiplication(a, b): return a * b
def division(a, b):
    if b == 0:
        return 'Error: Cannot divide by zero! Returning to options...'
    return a / b
def power(a, b): return a ** b
def root(a, b):
    if b == 0:
        return 'Error: Cannot divide by zero! Returning to options...'
    if a < 0:
        return 'Error: Cannot take root of negative number! Returning to options...'
    return a ** (1 / b)
def integer_division(a, b):
    if b == 0:
        return 'Error: Cannot divide by zero! Returning to options...'
    return f'Quotient: {a // b}, Remainder: {a % b}'

# Advanced functions
def factorial(a):
    if a < 0:
        return 'Error: Factorial not defined for negatives!'
    return math.factorial(a)
def percentage(a, b):
    if b == 0:
        return 'Error: Cannot divide by zero! Returning to options...'
    return (a / b) * 100
def logarithm(a, b):
    if a <= 0 or b <= 0 or b == 1:
        return 'Error: Invalid input for logarithm!'
    return math.log(a, b)
def sine(angle): return math.sin(math.radians(angle))
def cosine(angle): return math.cos(math.radians(angle))
def tangent(angle):
    if angle % 180 == 90:
        return 'Error: Tangent undefined at this angle!'
    return math.tan(math.radians(angle))

# Statistics helpers
def get_numbers():
    raw = input('Enter numbers separated by commas: ')
    return [float(x.strip()) for x in raw.split(',')]
def stats_min(nums): return min(nums)
def stats_max(nums): return max(nums)
def stats_abs(a): return abs(a)
def stats_mean(nums): return statistics.mean(nums)
def stats_median(nums): return statistics.median(nums)
def stats_mode(nums):
    try:
        return statistics.mode(nums)
    except statistics.StatisticsError:
        return 'No unique mode'
def stats_range(nums): return max(nums) - min(nums)
def stats_quartiles(nums):
    sorted_nums = sorted(nums)
    q2 = statistics.median(sorted_nums)
    mid = len(sorted_nums) // 2
    if len(sorted_nums) % 2 == 0:
        lower_half = sorted_nums[:mid]
        upper_half = sorted_nums[mid:]
    else:
        lower_half = sorted_nums[:mid]
        upper_half = sorted_nums[mid+1:]
    q1 = statistics.median(lower_half)
    q3 = statistics.median(upper_half)
    return q1, q2, q3
def stats_iqr(nums):
    q1, _, q3 = stats_quartiles(nums)
    return q3 - q1

# Main calculator loop
def calculator():
    while True:
        time.sleep(1)
        print('\n--- Calculator Menu ---')
        print('1. Add')
        print('2. Subtract')
        print('3. Multiply')
        print('4. Divide')
        print('5. Power')
        print('6. Root')
        print('7. Integer Division (Quotient & Remainder)')
        print('8. Statistics')
        print('9. Other (Advanced Functions)')
        print('0. Exit')

        choice = input('Type a number from 0 to 9: ')

        if choice == '0':
            print('Are you sure you want to exit?')
            print('1. Yes')
            exit = input('0. No ')
            if exit == '1': break
            else: print('Going back...'); time.sleep(1)

        elif choice == '1': print('Result:', addition(int(input('First addend: ')), int(input('Second addend: '))))
        elif choice == '2': print('Result:', subtraction(int(input('Minuend: ')), int(input('Subtrahend: '))))
        elif choice == '3': print('Result:', multiplication(int(input('First factor: ')), int(input('Second factor: '))))
        elif choice == '4': print('Result:', division(int(input('Dividend: ')), int(input('Divisor: '))))
        elif choice == '5': print('Result:', power(int(input('Base number: ')), int(input('Exponent: '))))
        elif choice == '6': print('Result:', root(int(input('Number: ')), int(input('Root (e.g. 2): '))))
        elif choice == '7': print(integer_division(int(input('Dividend: ')), int(input('Divisor: '))))
        elif choice == '8': statistics_menu()
        elif choice == '9': advanced_menu()
        else: print('Invalid choice. Pick a number from 0 to 9.')

# Statistics menu now directly accessible
def statistics_menu():
    while True:
        time.sleep(1)
        print('\n--- Statistics Menu ---')
        print('1. Minimum')
        print('2. Maximum')
        print('3. Absolute Value')
        print('4. Mean')
        print('5. Median')
        print('6. Mode')
        print('7. Range')
        print('8. Quartiles')
        print('9. IQR')
        print('0. Return to Main Menu')

        choice = input('Pick a number from 0 to 9: ')

        if choice == '0': break
        elif choice == '1': print('Minimum:', stats_min(get_numbers()))
        elif choice == '2': print('Maximum:', stats_max(get_numbers()))
        elif choice == '3': print('Absolute:', stats_abs(float(input('Enter number: '))))
        elif choice == '4': print('Mean:', stats_mean(get_numbers()))
        elif choice == '5': print('Median:', stats_median(get_numbers()))
        elif choice == '6': print('Mode:', stats_mode(get_numbers()))
        elif choice == '7': print('Range:', stats_range(get_numbers()))
        elif choice == '8':
            q1, q2, q3 = stats_quartiles(get_numbers())
            print('Q1:', q1, '| Q2:', q2, '| Q3:', q3)
        elif choice == '9': print('IQR:', stats_iqr(get_numbers()))
        else: print('Invalid choice.')

# Advanced menu now trimmed
def advanced_menu():
    while True:
        time.sleep(1)
        print('\n--- Advanced Functions ---')
        print('1. Factorial')
        print('2. Percentage')
        print('3. Logarithm')
        print('4. Sine')
        print('5. Cosine')
        print('6. Tangent')
        print('0. Return to Main Menu')

        choice = input('Type a number from 0 to 6: ')

        if choice == '0': break
        elif choice == '1': print('Result:', factorial(int(input('Number: '))))
        elif choice == '2': print(f'Result: {percentage(float(input("Part (a): ")), float(input("Whole (b): ")))}%')
        elif choice == '3': print('Result:', logarithm(float(input('Number: ')), float(input('Base: '))))
        elif choice == '4': print('sin =', sine(float(input('Angle in degrees: '))))
        elif choice == '5': print('cos =', cosine(float(input('Angle in degrees: '))))
        elif choice == '6': print('tan =', tangent(float(input('Angle in degrees: '))))
        else: print('Invalid choice.')

calculator()
