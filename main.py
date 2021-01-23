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

rps = [rock, paper, scissors]

import random

comp_choice_num = random.randint(0,2)
comp_choice = rps[comp_choice_num]

player_choice_num = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

player_choice = rps[player_choice_num]

print(player_choice)

print("Computer chose:\n" + comp_choice)

if player_choice_num == comp_choice_num:
  print("Draw!")
elif player_choice_num == 0:
  if comp_choice_num == 1:
    print("Youl lose.")
  else:
    print("You win.")
elif player_choice_num == 1:
  if comp_choice_num == 0:
    print("You win.")
  else:
    print("You lose.")
elif player_choice_num == 2:
  if comp_choice_num == 0:
    print("You lose.")
  else:
    print("You win.")