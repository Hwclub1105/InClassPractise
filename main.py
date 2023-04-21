import sys

'''
Pseudocode

win = [7,11]
loose = [2,3,12]

name = USERINPUT
REPEAT 
    num1 = RANDOM(1,6)
    num2 = RANDOM(1,6)
    total = num1 + num2
    OUTPUT total
UNTIL total in valid
IF total in win
    OUTPUT 'You win'
ELSE
    OUTPUT 'You Lost'

'''
from random import randint #Import random library

name = input('Enter your name: ') #Allow user to enter name

def Menu(mode):
    if mode == 'start':
        return input('1) Roll          2) Quit\n')
    else:
        return input('1) Restart       2) Quit\n')

while True:
    while True: #Loop
        if Menu('start') == '2':
            break
        die1 = randint(1,6) #Generate 2 dice throws and getiing the total
        die2 = randint(1,6)
        total = die1 + die2 
        
        print(total)
        
        if (total == 7) or (total == 11): #Check if the total is equal to the winning conditions
            print(name,'you have won ')
            if Menu('restart') == '2':
                sys.exit('Bye Bye')
        elif (total == 2) or (total == 3) or (total == 12): #Check if the total is equal to the loosing conditions
            print(name,'you lost ')
            break
        
    
    