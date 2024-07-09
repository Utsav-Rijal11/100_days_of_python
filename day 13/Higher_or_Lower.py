import os 
import random
from Higher_or_lower_logos import logo_1,logo_2
from game_data import data



def get_random_account():
    return random.choice(data)

def format_data(account):
    name=account["name"]
    description=account["description"]
    country=account["country"]
    return name,description,country

def check_answer(guess, follower_count_account_A, follower_count_account_B):
    if follower_count_account_A> follower_count_account_B:
        if guess=="a":
            return True
        else:
            return False
    elif follower_count_account_A<follower_count_account_B:
        if guess=="a":
            return False
        else:
            return True



def game():
    score=0
    print(logo_1)
    game_over=False
    Account_A=get_random_account()
    Account_B=get_random_account()
    while not game_over:
        Account_A=Account_B
        Account_B=get_random_account()

        while Account_A==Account_B:
            Account_B=get_random_account()
        
        print(f"Compare A: {format_data(Account_A)}.")
        print(logo_2)
        print(f"Against B: {format_data(Account_B)}.")
        guess=input("who has more followers? Type A or B:").lower()
        follower_count_account_A=Account_A["follower_count"]
        follower_count_account_B=Account_B["follower_count"]
        is_correct=check_answer(guess, follower_count_account_A, follower_count_account_B)

        os.system("cls")
        print(logo_1)

        if is_correct==True:
            score+=1
            print(f"You're right! The score is {score}")

        else :
            game_over=True
            print(f"Sorry, that's wrong. Final score: {score}")

game()







