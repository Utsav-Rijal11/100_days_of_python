import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')
display = []
for no_of_letters in range(len(chosen_word)):
    display += "_"
print(display) 
end_of_game=False 
lives=6
while end_of_game==False:  
    guess= input("Guess a letter : ").lower()
    for position in range (0,len(chosen_word)):
       # extra_variable=chosen_word[position]
        if chosen_word[position]==guess:
            display[position]=guess
    if guess not in chosen_word:
        lives-=1
                
    print(display)
    print(f"lives={lives}")
    if lives==0:
        print("You lost.")
        end_of_game=True
    
    if "_" not in display :
        end_of_game=True
        print("You won.")   
