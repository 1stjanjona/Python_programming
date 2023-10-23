#!/usr/bin/env python3
my_guess = int(input("Please guess a number: \n"))
correct_guess = 20
if my_guess > 0 and my_guess  < 21:
    if my_guess == correct_guess:
        print("Bingo, you guessed it rigth")
    else:
        print(f"The rigth guess is {correct_guess} and your guess was {my_guess}.")
else:
    print(f"Your guess was: {my_guess}, but the rigth guess is lesser than 21. Guess again!")
