#Data Type Casting in Python
#Taking input from Users in Python
"""
1-Python is an Object Orientaed Language and it uses classes to define 
Data Types
2-Casting therefore can be done using Constructor Function  
"""

#Casting data into Integer int()
'''
1-constructs an integer number from a float literal 
    (by rounding down to the previous whole number) 
2-constructs an integer number from a string literal 
    (providing the string represents a whole number)
'''
'''
marks = 125.75
name="Name1"
age = "45"
#print(int(marks))
print(int(age))
'''

#Casting data into Float float()
''' 
1-constructs a float number from an integer literal 
2-constructs a string literal 
    (providing the string represents a float or an integer)
'''

age=20

#print(age)
#print(float(age))
'''
marks1 = "12.45"
marks2="60"

print(type(marks1))
print(type(marks2))

print(type(float(marks1)))
print(type(float(marks2)))
'''

#Casting Data into String str()
'''
1-constructs a string from a wide variety of data types, 
    including strings, integer literals and float literals
'''
'''
totol_marks=100.12
print(type(totol_marks))
print(type(str(totol_marks)))
'''

#Taking input from Users
num1 = int(input("Enter first number : ")) #By default string format
num2 = int(input("Enter second number : "))
num_sum = num1+num2
print("Your age is " + str(num_sum))








