# computer guesses a number between 1 and 100
# user tries to guess this number
# if guess is lower than the number then:
# the program informs guess higher
# else if the number is higher, then:
# the program informs guess lower

import random

number_target = random.randint(1, 1000)

number_of_guesses = 0

while True:
    number_guess = int(input("Guess a number between 1 and 1000: "))
    number_of_guesses += 1

    if number_guess == number_target:
        print(f"You won after {number_of_guesses} tries!")
        break
    elif number_guess < number_target:
        print("Guess higher")
    elif number_guess > number_target:
        print("Guess lower")
    
