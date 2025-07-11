import random
import time

print('Wheel of Names')

while True:
    amount = input('How many names/choices should there be? ')

    if amount.isdigit():
        amount = int(amount)
        if amount < 1:
            print('Error: Invalid amount! Returning to options...')
        else:
            break
    else:
        print('Error: Please enter a number, not letters or symbols.')

while True:
    wheel = []
    print('')
    print('Enter the names:')
    for count in range(1, amount + 1):
        enter = input(str(count) + '. ')
        wheel.append(enter)
    print('')
    print('Your choices:')
    for verify in range(amount):
        print(wheel[verify])
    print('')
    print('1. Confirm')
    confirm = input('0. Choose again ')
    if confirm == '0':
        print('Going back...')
    elif confirm == '1':
        break

print('')
print('🎡 The wheel is ready...')
time.sleep(1)
print('Starting in...')
for i in range(3, 0, -1):
    print(i)
    time.sleep(1)

print('')
print('Spinning...')
time.sleep(0.5)
for i in range(10):
    fake_spin = random.choice(wheel)
    print('➡️', fake_spin)
    time.sleep(0.3)

winner = random.choice(wheel)
print('')
print('✨ And the winner is...')
time.sleep(1.5)
print('🥳', winner, '🥳')
