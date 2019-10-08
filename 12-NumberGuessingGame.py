import random
#Number Guessing Game
'''
1-Random Library
2-User Input
3-DataType Casting
4-While Loop
5-If - Else
'''
secret_num = random.randrange(1,5) 
your_guess = 0   
guess_count = 0
max_guesses = 3
has_more_guess = True

while int(your_guess) != secret_num and has_more_guess:
    if guess_count < max_guesses:
        your_guess = input("Enter Your Guess Number : ")
        guess_count+=1 #guess_count = guess_count + 1
    else:
        has_more_guess = False    


if not(has_more_guess):
    print("You are out of Guesses. You lost the game")
else:    
    print("You win!")