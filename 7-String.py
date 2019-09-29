#String literals in python are surrounded by either 
'''
single quotation marks e.g. name='MyName'
double quotation marks e.g. name="MyName"
tripple quotation marks e.g. name="""MyName"""
'''


greeting = 'Good Evening!'
greeting1 = 'Good Evening!'
greeting2 = "Good Evening!"
greeting3 = '''Good Evening!'''
greeting4 = """Good Evening!"""

#To get the type of data
print(type(greeting1))
print(type(greeting2))
print(type(greeting3))
print(type(greeting4))

#To get the actula data inside the variable
print(greeting1)
print(greeting2)
print(greeting3)
print(greeting4)


#String literal can be displayed with the print() function

#Assign String to a Variable e.g. a="any string"
#assignment happence from right to left

greeting = 'Good Evening!'

#Multiline Strings


greeting = '''Good Evening!
one more line!!!'''
print(greeting)


#Strings are Arrays
print(greeting[0])
print(greeting[1])
print(greeting[2])
print(greeting[3])

#Slicing
print(greeting[5:12])

#Negative Indexing
print(greeting[-8:-1])
#String Length
print("Length of the string is ", len(greeting))


#String Methods
'''
1-The strip() method removes any whitespace from the beginning or the end
2-The lower() method returns the string in lower case
3-The upper() method returns the string in upper case
4-The replace() method replaces a string with another string
5-The split() method splits the string into substrings if it finds instances of the separator
6-To check if a certain phrase or character is present in a string, we can use the keywords in or not in
7-To concatenate, or combine, two strings you can use the + operator
8-To add a space between them, add a " "
9-The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are
'''


print(greeting.strip())
print(greeting.lower())
print(greeting.upper())
print(greeting.replace("Good","Happy"))
print(greeting.split(" "))

x = "Go" not in greeting  
print(x)

g1="Good"
g2="Evening"
greeting =g1+" "+g2+"!"
print(greeting)

qty=3
item=17
price=35.75

myOrder = "I want {0} pieces of item {1} for {2} rupees"
print(myOrder.format(qty,item,price))

