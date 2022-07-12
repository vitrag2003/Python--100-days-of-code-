#Higher-Lower game 
import os 
import random 
import art 
from game_data import data

def check_answer(account1_followers,account2_followers,guess):
    if account1_followers>account2_followers:
        return guess=="a"
    else:
        return guess=="b" 

print(art.logo)

game_streak=True
score=0
account2=random.choice(data) 

while game_streak:

    account1=account2
    account2=random.choice(data) 
    if account1==account2:
        account2=random.choice(data)

    account_name1=account1["name"]
    account_desc1=account1["description"]
    account_country1=account1["country"]
    print(f"\n\nCompare A: {account_name1}, a {account_desc1} from {account_country1}")

    print(art.vs)

    account_name2=account2["name"]
    account_desc2=account2["description"]
    account_country2=account2["country"]
    print(f"Against B: {account_name2}, a {account_desc2} from {account_country2}")

    account1_followers=account1["follower_count"]
    account2_followers=account2["follower_count"]

    guess=input("Who has more followers? Type 'A' or 'B': ").lower()

    is_correct=check_answer(account1_followers,account2_followers,guess)

    if is_correct:
        score=score+1
        print(f"You are RIGHT! Current score: {score}")
        os.system('cls')
    else:
        print(f"You are WRONG! Final score: {score}")
        game_streak=False
