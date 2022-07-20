
import random
from hangman_art import logo,stages
from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

print(f'Pssst, the solution is {chosen_word}.')

display = []
for i in chosen_word:
  display.append('_')

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed the letter {guess}")
    for i in range(len(chosen_word)):
        if guess in chosen_word[i]:
            display[i]=guess

    if guess not in chosen_word:
        print(f"The letter {guess} is not present in the word, you lose a life")
        lives-=1
        if lives==0:
            print("You Lose")
            end_of_game = True

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])