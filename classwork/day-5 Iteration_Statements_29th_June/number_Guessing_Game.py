'''
Number Guessing Game
Problem Statement
A secret number is 37.
Keep asking the user to guess the number until the correct number is entered.
Display whether the entered number is too high, too low, or correct'''
secret_number = 37
while True:
    guess = int(input("Guess the number: "))
    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Correct! The secret number is 37.")
        break
    