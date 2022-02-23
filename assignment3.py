# Assignment 3 - Writing code from a design (Ifs/Modules/Loops)
#
#  I Benjamin Thompson, 000843991, certify that this work is my own effort
#  and that I have not allowed anyone else to copy from it.





#module that picks a secret number and determines a user input being lower or higher

#function name: checkGuess
#Input user_number (integer) secret_number(integer)
#output: result (integer) 1, 0, -1 


import random

def checkGuess(userInput, secretNumber):
    if userInput > secretNumber:
        total = -1
    elif userInput < secretNumber:
        total = 1
    elif userInput == secretNumber:
        total = 0
    return (total)
   

   
#main module

#input: user_number(integer), username(string)

#output: ("Enter a username: "),("Hello", username, "welcome to the guessing game."), ("What is your guess?"), ("Enter a guess: "),("Your guess", userInput, "was too high!"), ("Your guess", userInput, "was too low!"),("Amazing! On your first guess!"),
#("Excellent! On second guess!"), ("Lucky! On your last guess!"), ("Thank you for playing", username, "your score was", score, "points.")   

#variables: guesses, secretNumber, score, username, userInput


username = (input("Enter a username: "))
#Assume the user enters a username should be a string but it seems numbers work also
score = 0
secretNumber = len(username)*random.randint(1,5)
#calculates a secret number based on the players username
guesses = 0
print ("Hello", username, "welcome to the guessing game.")


while guesses < 3:
    remaining = 3 - guesses
    print ("You have", remaining, "guesses left")
    print ("What is your guess?")
    userInput = int(input("Enter a guess: "))
    #Assume the user enters an integer as a guess
    guesses = guesses + 1
    checkGuess(userInput, secretNumber)
    #calls my checkGuess function
    result = checkGuess(userInput, secretNumber)
    if result == 0:
        if guesses == 1:
            print("Amazing! On your first guess!")
            score = score + 10
            break
        else:
            if guesses == 2:
                print ("Excellent! On second guess!")
                score = score + 5
                break
            else:
                print("Lucky! On your last guess!")
                score = score + 1
                break
    else:
        if result == 1:
            print ("Your guess", userInput, "was too low!")

        else:
            print("Your guess", userInput, "was too high!")


print ("Thank you for playing", username, "your score was", score, "points.")   
