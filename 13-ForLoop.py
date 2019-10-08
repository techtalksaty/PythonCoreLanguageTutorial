'''
#Iteration on string
names = "name1#"
for character in names:
    print(character.upper())
'''
'''
#Iteration on List
name_list = ["name1","name2","name3","name4","name2"]

for name in name_list:
    print(name)
'''
'''
#Break Statement
name_list = ["name1","name2","name3","name4","name2"]
for name in name_list:
     print(name)
    if name=="name3":
        break
'''   

'''
#Continue Statement
name_list = ["name1","name2","name3","name4","name5"]
for name in name_list:    
    
    if name=="name3":
        print("This is before continue!")
        continue
    print(name)
'''
'''
for i in range(0,10,3):
    print(i)
else:
    print("Lood has ended!")
'''
'''
colors = ["Red","Yellow","Pink"]
fruits = {"Red":"Apple","Yellow":"Banana","Pink":"Cherry"}

for color in colors:
    for fruit in fruits:
        if color==fruit:
            print(color,fruits[color])
'''
#print(fruits["Red"])
























