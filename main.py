#A retry pops up when you enter a string, decimal or negative number. The points are accumulated and you can continue or finish it when you want.
#It's a number guessing mini-game


import random

def number_guessing(points_counter=None):
    bot = random.randint(2,2)
    points = random.randint(1,3)
    if points_counter == None:
        points_counter = 0

    try:
        number = int(input("Write a number from 1 to 10: " ))
        if number < 0:
            print("Sorry, no number below 0, try again")
            number_guessing(points_counter)
    except ValueError:
        print("Please enter a number between 1-10, no strings or decimals.")
        number_guessing(points_counter)
    
    else:
        if number == bot:
            print(f"Congratulations! you guessed right: {bot}")
            points_counter = points_counter+points
            print(f"You have {points_counter} points!")  

        elif number != bot:
            print(f"You are wrong it was {bot}, but don't be sad, try again!")

        keep_playing = input("Would you like to play again? Y/N: ").lower()

        if keep_playing == "y":
            number_guessing(points_counter)              
                
        elif keep_playing == "n":
            print("Thanks for playing!")
                
number_guessing()
