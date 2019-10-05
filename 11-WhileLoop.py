#What is a Loop?
'''
A loop is a sequence of instructions that is continually repeated 
until a certain condition is reached.

Python has two primitive loop commands/constructs
1-While Loop
2-For Loop   
'''

'''
print(1)
print(2)
print(3)
print(4)
print(5)
'''

'''
x=0 #Step-1 Initialization
while x<10: #Step-2 Loop Condtion 
    print(x) #Step-3 Business Logic
    x+=1 #Step-4 Increament / Decreament 
'''
'''
#Break
x=0
while x<10:
    print(x)
    if x==4:
        break
    x+=1
'''

'''
#Continue
x=0
while x<10:
    x+=1
    if x==4:
        continue
    print(x)
'''

'''
#Else
x=0
while x<10:
    print(x)
    x+=1
else:
    print("x is no longer less than 10")    
'''
    































