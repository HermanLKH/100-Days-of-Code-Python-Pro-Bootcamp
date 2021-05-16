# Rock, paper, scissors

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
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))

if user_choice > 2:
  print("You typed an invalid number, you lose!")
else:
  user_choice = game_images[user_choice]
  npc_choice = random.choice(game_images)
  print(user_choice)
  print(f"Computer choose\n{npc_choice}")
  if user_choice == npc_choice:
    print("It's a tie!")
  elif user_choice == rock and npc_choice == scissors:
    print("You win!")
  elif user_choice == paper and npc_choice == rock:
    print("You win!")
  elif user_choice == scissors and npc_choice == paper:
    print("You win!")
  else:
    print("You lose...")