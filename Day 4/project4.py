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
user_choice=int((input("Enter (1) for Rock (2) for paper and (3) for scissors\n")))
if user_choice==1:
    print(rock)
elif user_choice==2:
    print(paper)
elif user_choice==3:
    print(scissors)
print("Computer chose")
comp_choice=random.randint(1,3)
if comp_choice==1:
    print(rock)
elif comp_choice==2:
    print(paper)
elif comp_choice==3:
    print(scissors)

if user_choice>=0 or user_choice<0:
    print("Inavalid choice! You Lose :(")
elif (user_choice==1 and comp_choice==3) or (user_choice==3 and comp_choice==2) or (user_choice==2 and comp_choice==1):
    print("Hooray! You Won")
elif user_choice==comp_choice:
    print("It's a draw")
else:
    print("You lose :(")