import math
# CODE TO SOLVE QUADRATIC EQUATION

a = float(input('give the value of a '))        
b = float(input('give the value of b '))       
c = float(input('give the value of c '))

d = pow(b,2)-(4*a*c)

x1 = (-b + math.sqrt(d))/(2*a)

x2 = (-b - math.sqrt(d))/(2*a)

print ('x1 =', x1)
print ('x2 =', x2)

"""
Note:
import cmath # To calculate complex function, replace the math module above with cmath module when solving complex function.
"""
