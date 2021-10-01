import random

print('This is a number guessing game')
randNum = random.randint(1,10)
chances = 5

while chances>0:
    num = int(input('Enter a number from 1 to 10: '))

    if num>randNum:
        print('The number you entered is greater')

    elif num<randNum:
        print('The number you entered is lesser')

    else:
        print('You are correct')
        break
    
    chances-=1

if chances==0:
    print('you lose, the number was',randNum)
    