#There are three numeric types in Python
    #int
    #float
    #complex
#Variables of respective Numeric types are created when you assign a value to them
#You can verify the type of any object in Python using the type() function


#1-Int
'''Int or Integer is a whole number 
positive and negative
without decimal
Unlimited length
'''
'''
x=1
y=6578657546789765
z=-80

print(type(x))
print(type(y))
print(type(z))
'''

#Float
'''
Float or 'floating point number' is a number
positive or negative
containing one or more decimals
Float can also be scientific numbers with an "e" to indicate the power of 10.
'''
'''
x=1.45765487645
y=2364283749823471.01
z=-3.76

print(type(x))
print(type(y))
print(type(z))

x=45e3 #45*10*10*10
y=15e15 # 15 * 10*10*10 up to 15 times
z=-3.76e5

print(type(x))
print(type(y))
print(type(z))
'''

#Complex
'''
Complex numbers are written with a "j" as the imaginary part.
'''
'''
x=3+4j
y=6j
z=-7j

print(type(x))
print(type(y))
print(type(z))
'''

#Type Conversion
'''
You can convert from one type to another with the int(), float(), and complex() methods
'''
#Conversion of Int into float and complex
#x=10
#print(type(x))
#print(type(float(x)))
#print(type(complex(x)))
#print(float(x))
#print(complex(x))

#Conversion of Float into Int and complex
'''
x=10.98
print(type(x))
print(type(int(x)))
print(type(complex(x)))
print(int(x))
print(complex(x))
'''

#You cannot convert complex numbers into another number type
'''
x=3+4j
print(int(x))
print(float(x))
'''

'''
import random #always use import on the top of the program
print(random.randrange(1,10))
'''







