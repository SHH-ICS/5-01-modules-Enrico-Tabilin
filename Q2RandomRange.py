# Create a program that accepts 2 numbers from the user. 
# Your program will output a random number between the range given by the user.
import random
try:
    x=int(input('Enter integer 1 (bottom value): '))
except:
    print('Please re-run the program and enter a valid number.');exit()
try:
    y=int(input('Enter integer 2 (top value):'))
except:
    print('Please re-run the program and enter a valid number.');exit()
if x>y:
    print('Please re-run the program and enter a smaller first value.')
else:
    print('Your random number is:',random.randint(x,y))