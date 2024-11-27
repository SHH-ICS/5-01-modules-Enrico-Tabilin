# Create a program that will ask the user an addition question. 
# The program will generate two random numbers between 1 and 100, and display them as an addition question with appropriate prompts.
import random
z=''
streak=0
s=-1
print('Type "EXIT" to quit.')
while True:
    while z=='':
        if streak==s+1:
            x=random.randint(1,100+10*streak)
            y=random.randint(1,100+10*streak)
            s=streak
            cases=[x+y,x-y,x*y]
            casetype=random.randint(0,0+int(streak/10))
            attempt=1
        try:
            if casetype==0:
                z=input('Solve '+str(x)+'+'+str(y)+': ')
            elif casetype==1:
                z=input('Solve '+str(x)+'-'+str(y)+': ')
            else:
                z=input('Solve '+str(x)+'*'+str(y)+': ')
            z=int(z)
        except:
            if z=="EXIT":
                exit()
            else:
                print("You didn't even give a valid integer!")
                z=''
        while z!='':
            if z==cases[casetype]:
                streak=streak+1
                print('Correct! Your current answer streak is',str(streak)+'!')
                z=''
            else:
                if attempt>4:
                    print('Incorrect! The answer was',str(cases[casetype])+'. Nice try! Your answer streak was',str(streak)+'.');exit()
                else:
                    attempt=attempt+1
                    print('Incorrect! Try again.',(abs(6-attempt)),'attempts left.')
                    z=''