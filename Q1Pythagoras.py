# Create a program that will accept the two legs of a right-angle triangle, a and b, and display the length of the hypotenuse, c. 
# Remember to use prompts for the input and labels for the output. Use the formula a2 + b2 = c2 to calculate your answer.
import math
try:
    a=float(input('Enter the input for a: '))
except:
    print('Error! Input invalid. Please re-run the program and enter a float value.');exit()
try:
    b=float(input('Enter the input for b: '))
except:
    print('Error! Input invalid. Please re-run the program and enter a float value.');exit()
c=math.sqrt(a**2+b**2)
print('The square root of',a,'+',b,'=',c,'('+str(round(c,3))+' rounded)')