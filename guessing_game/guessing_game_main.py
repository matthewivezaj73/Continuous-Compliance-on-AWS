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
        