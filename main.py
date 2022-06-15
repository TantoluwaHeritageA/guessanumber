# Steps
# - a variable that stores the random number
# - an input that asks the user what level to pick
# - a variable that stores response of the level of the user
# - an if condition to check if the user chose easy or hard level
# - if user picks easy level, a variable called attempt is created and set to 10
# - and input that asks user for their guesses
# - another variable that compares the fixed number and the user's guess
# if user picks hard level , a variable called attempt is created and set to 5
# - input that asks user for their guesses
# - another variable that compares the fixed number and the user's guess

# Methods
# - while loop|
# - for loop with range
# - functions
# - input method


# code starts here
import random
from art import logo
fixed_number = random.randint(1, 100)
# easy_attempt = 10
# hard_attempt = 5
print(fixed_number)


def welcome():
    print(logo)
    print(''' 
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.''')


welcome()


def start_guess(user_prompt):
    easy_attempt = 10
    hard_attempt = 5
    if user_prompt == "easy":
        print("You have 10 attempts remaining to guess the number")
        while easy_attempt > 0:
            user_guess = int(input("Make a guess: "))
            if user_guess == fixed_number:
                print(f"You got it ,The answer was {fixed_number}")
                break
            else:
                easy_attempt -= 1
                if user_guess > fixed_number:
                    print("Too high")
                elif user_guess < fixed_number:
                    print("Too low")
                if easy_attempt == 0:
                    print("You've run out of guesses, you lose")
                print(
                    f"You have {easy_attempt} attempts remaining to guess the number")
    elif user_prompt == "hard":
        print("You have 5 attempts remaining to guess the number")
        while hard_attempt > 0:
            user_guess = int(input("Make a guess: "))
            if user_guess == fixed_number:
                print(f"You got it ,The answer was {fixed_number}")
                break
            else:
                hard_attempt -= 1
                if user_guess > fixed_number:
                    print("Too high")
                elif user_guess < fixed_number:
                    print("Too low")
                if hard_attempt == 0:
                    print("You've run out of guesses, you lose")
                print(
                    f"You have {hard_attempt} attempts remaining to guess the number")


start_guess(input("Choose a difficulty. Type 'easy' or 'hard': "))
