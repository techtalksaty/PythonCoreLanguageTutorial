#If statement is used to check for certain condition in Python
'''
num1 = 500
num2 = 500

if num1>num2:
    print(num1, "is greater than",num2)

elif num2>num1:
    print(num2, "is greater than",num1) 

else:
    print("both numbers are equal")    
'''

#IsValid=False

'''
if IsValid:
    print("This is valid")
else:
    print("This is not valid")
'''

#print("This is valid") if IsValid else print("Not valid") 
'''
x=37
y=37

print(x) if(x>y) else print("Equal")if(x==y)else print(y)
'''
'''
a=100
b=500
c=90

if a>b and c>a:
    print("Both conditions are true")
else:
    print("One of the condition is false")


if not(a>b or c>a):
    print("One of the conditions is true")
else:
    print("Both condition are false")
'''

'''
num1 = input("Input First Number : ")
num2 = input("Input Second Number : ")

if(num1.isnumeric() and num2.isnumeric()):
    if(int(num1)>int(num2)):
        print(num1,"is greater than", num2)
    elif(num2>num1):
        print(num2,"is greater than", num1)
    else:
        print("both numbers are equal and the number is", num1)    
else:
    print("Invalid Input")
'''
