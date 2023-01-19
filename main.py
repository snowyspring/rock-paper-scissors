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


user_choice=input("What do you choose? Type 0 for Rock, 1 for Paper or  2 for Scissors. \n")
import random

list= [rock, scissors,paper]
computer_choice = random.choice(list)
if user_choice == "0":
  print(rock)
elif user_choice == "1":
  print(paper)
elif user_choice == "2":
  print(scissors)

print("Computer chose:")
print(computer_choice)

if user_choice == "0":
  if computer_choice ==rock:
    print("You draw.")
  elif computer_choice ==paper:
    print("You lose.")
  elif computer_choice == scissors:
    print("You win.")
  
elif user_choice == "1":
  if computer_choice == rock:
    print("You win.")
  elif computer_choice == paper:
    print("You draw.")
  elif computer_choice == scissors:
    print("You lose.")
  
elif user_choice == "2":
  if computer_choice == rock:
    print("You lose.")
  elif computer_choice == paper:
    print("You win.")
  elif computer_choice == scissors:
    print("You draw.")