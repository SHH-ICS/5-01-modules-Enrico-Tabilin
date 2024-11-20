# Create a program that will ask the user an addition question. 
# The program will generate two random numbers between 1 and 100, and display them as an addition question with appropriate prompts.
import random
x=random.randint(1,100)
y=random.randint(1,100)
try:
    z=int(input('Solve '+str(x)+'+'+str(y)+': '))
except:
    print("You didn't even give a valid integer! The answer to this problem was",x+y);exit()
if z==x+y:
    print('Correct! You get a virtual pat on the back.')
else:
    print('Incorrect! The answer was',x+y)