import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word=random.choice(word_list)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess=input("Guess a letter:").lower()
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in chosen_word:
  if guess==letter:
    print("right")
  else:
    print("wrong")
# chosen_word=word_list[random.randint(0,len(word_list)-1)]
#  print(word)
# guess=input("Guess a letter:").lower()
# for i in range(len(chosen_word)):
#   if guess in chosen_word[i]:
#     print("right")
#   else:
#     print("wrong")