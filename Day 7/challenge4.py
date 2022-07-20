#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
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
chosen_word = random.choice(word_list)
lives=6
# word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')
#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
#Create blanks
display = []
for i in chosen_word:
  display.append('_')

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
#while '_' in display: 
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for i in range(len(chosen_word)):
        if guess in chosen_word[i]:
            display[i]=guess
    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    
#Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    if guess not in chosen_word:
        lives-=1
        print(stages[lives])
        if lives==0:
            print("You Lose")
            end_of_game = True
    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.