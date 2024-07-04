import random
print("\nWelcome to hangman!\n This is completely random.\nI'll help you decide your fate.\n")
from hangman_words import word_list
chosen_word = random.choice(word_list)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')
display = []
for no_of_letters in range(len(chosen_word)):
    display += "_"
print(display)  
lives=6
while "_" in display:  
    guess= input("Guess a letter : ").lower()
    if guess not in chosen_word:
        lives-=1
        from hangman_art import stages
        print(stages[lives])  
    else:
        for position in range (0,len(chosen_word)):
            if chosen_word[position]==guess:
                display[position]=guess
    if lives==0:
        print("you lost!")
        print(f"the word was={chosen_word}")
        break
    

                
    print(display)
    print(f"lives={lives}")
if "_" not in display :
    print(f"the word is : {' '.join(display)}")
    print("You won.")
    
