print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name = name1 + name2
name = name.lower()
true = name.count('t')+name.count('r')+name.count('u')+name.count('e')
love = name.count('l')+name.count('o')+name.count('v')+name.count('e')
true_love = str(true)+str(love)
love_score = int(true_love)
if love_score<10 or love_score>90:
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif love_score>=40 and love_score<=50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"your score is {love_score}")