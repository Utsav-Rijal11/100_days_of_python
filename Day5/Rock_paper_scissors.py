import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
options=[rock,paper,scissors]
user_choice = int(input("Enter your choice:\n press 0 for rock\n 1 for papers\n 2 for scissors."))
print("user_choice is:")
print(options[user_choice])
computer_choice =random.randint(0,2)
print("computer choice is:")
print(options[computer_choice])

if user_choice<0 or user_choice>=3 :
    print("invalid user's choice.")
elif user_choice==0 and computer_choice==2:
    print("You won.")
elif user_choice==2 and user_choice==0:
    print("computer won.")
elif user_choice>computer_choice:
    print("You won.")
elif user_choice<computer_choice:
    print("computer won.")
else:
    print("Match Drawn.")
    
    
                      




