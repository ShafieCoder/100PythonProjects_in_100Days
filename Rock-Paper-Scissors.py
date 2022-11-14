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


# rock (0) wins against scissors (2)
# scissors (2) win against paper (1)
# paper(1) win against rock(0)
import random
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)
game_images = [rock, paper, scissors]
print(game_images[player_choice])
print(f"Computer choice:\n {game_images[computer_choice]}")

if player_choice >= 3 or player_choice <0:
  print("You typed a wrong number!!")
elif player_choice == 0 and computer_choice == 2:
  print("You Won!")
elif computer_choice == 0 and player_choice == 2:
  print("You lost.")
elif player_choice > computer_choice:
  print("You won!")
elif player_choice == computer_choice:
  print("It is a draw.")
else:
  print("You lost.")
