#Booleans represents one of two values TRUE or FALSE
print(10==10)
print(type(10==10))

#Please note ======================================================
# = single equal sign is an assignment oprator
# == double equal sign is ancomparision oprator


#In programming we often need to know if an expression is TRUE or FALSE
name="Some Name"
name1="some NaMe"
#Use upper or lower function while string comparision
print(name.upper()==name1.upper())

#Expression evaluation results in TRUE or FALSE
#When you compare two values you get either TRUE or FALSE

#When you run a condition in if statement, Python returns TRUE or FALSE
if name.upper()==name1.upper():
    print("Matched")
else:
    print("Not Matched")    

#The bool() allows you to evaluate any value or give you TRUE or FALSE
print(bool(0)) #0 will print FALSE on console 
print(bool(1)) #Any number greater than 0 will print TRUE on console
print(bool("Name")) #All strings will print TRUE on console
print(bool("")) #Empty string will print FALSE on console

#Some common TRUE Values==============================================
#Almost any value is evaluated to True if it has some sort of content.
#Any string is True, except empty strings.
#Any number is True, except 0.
#Any list, tuple, set, and dictionary are True, except empty ones.

#Some common False Values=============================================
#In fact, there are not many values that evaluates to False 
#Except empty values, such as (), [], {}, "", the number 0
#And the value None. And of course the value False evaluates to False.
#The following will return False
#bool(False)
#bool(None)
#bool(0)
#bool("") Empty String
#bool(()) Empty Tupple
#bool([]) Empty List
#bool({}) Empty Dictionary