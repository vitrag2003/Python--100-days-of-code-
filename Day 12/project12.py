#Number guessing game 
import random

easy_level_turns=10 #global variable
hard_level_turns=5 #global variable

def check_answer(guess,number,turns_available):
    if guess>number:
        print("Too high")
        return turns_available-1
    elif guess<number:
        print("Too low")
        print("Guess again")
        return turns_available-1
    else:
        print("Correct guess")

def difficulty():
    choice=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if choice=="easy":
        return easy_level_turns
    else:
        return hard_level_turns

def game():
    print("Welcome to the NUumber guessing game")
    number=random.randint(1,100)
    print("I'm thinking of a number between 1 and 100.")
    turns_available=difficulty()
    guess=0
    while guess!=number:
        print(f"You have {turns_available} attempts remaining to guess the number")
        guess=int(input("Make a guess: "))
        turns_available=check_answer(guess,number,turns_available)
        if turns_available==0:
            print("You have run out of guesses, you lose.")
            exit()

game()