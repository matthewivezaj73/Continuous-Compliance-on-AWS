#Matthew Ivezaj
#6/14/2022
#Guessing Game
#Importing the function from guessing_game.py. 
from functions.guessing_game import guessing_game
#Creating a flag.
not_done = False
#Creating a random number.
my_rand = guessing_game()
#Testing for user input.
while not not_done:
    #Asking the user what number was generated.
    print("Please enter the random number:\t")
    #Accepting the user's guess on what the random number could be.
    user_guess = input("")
    #Handling the case where the user correctly guessed the number.
    if user_guess == my_rand:
        #Printing out a congratulations message to the user.
        print("Congratulations, your guess was correct!")
        #Setting the not_done flag to true to escape the loop.
        not_done = True
    #Handling the case where the user incorrectly guessed the number but is a numeric value.
    elif user_guess.isdigit():