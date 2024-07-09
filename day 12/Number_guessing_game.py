import os
import random
from guessing_game_logo import logo
print(logo)
print("!Welcome to number guessing game!\n")
#game_over=False
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
               21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 
               39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 
               57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 
               75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 
               93, 94, 95, 96, 97, 98, 99, 100]
number_to_be_guessed=random.choice(number_list)
def difficulty(choice):
    lifes=0
    if choice=="easy":
        lifes=10
        return lifes
    elif choice=="difficult":
        lifes = 5
        return lifes
    
def check(number,life):
    global number_to_be_guessed
    if number==number_to_be_guessed:
        print(f"You have guessed the number to be {number} and it's correct.")
        return 20
    elif number>number_to_be_guessed:
        life-=1
        print(f"Too high.Remaining lives={life}")
        return life
    elif number<number_to_be_guessed:
        life-=1
        print(f"Too low.Remaining lives={life}")
        return life

def game():
    game_over=False 
    game_level=input("Type Easy for easy mode and Difficult for difficult mode:").lower()
    lives=difficulty(game_level)
    print(f"Remaining lives={lives}")   
    while not game_over:
        #number_to_be_guessed=random.choice(number_list)
        #game_level=input("Type Easy for easy mode and Difficult for difficult mode:").lower()
        #lives=difficulty(game_level)
        #print(f"Remaining lives={lives}")
        if lives>0:
            #print(f"Remaining lives={lives}")
            user_guess=int(input("Enter your guess number:"))
            lives=check(user_guess,lives)
            if lives==20:
                break
            print(f"Remaining lives={lives}")
        elif lives==0:
            print("Game over!You lost")
            game_over=True
    user_choice=input("Do you want to play game again? Type y for yes and n fo no.").lower()    
    if user_choice=="y":
        os.system("cls")
        print(logo)
        game()
    else:
        os.system("cls")
        print("Thank you for playing the game.")

game()        
# you're the first one to win the difficult level
# none of my friends in class guessed it correctly LOL


    

        

    