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
game_images = [rock, paper, scissors]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)
print(f"User choice:\n {game_images[player_choice]}\n")
print(f"computer choice:\n {game_images[computer_choice]}\n")


if player_choice >= 3 or player_choice < 0:
    print("you typed the wrong number!")
elif player_choice == 0 and computer_choice == 2:
  print("Congratulation! You Won!")
elif player_choice == 2 and computer_choice == 1:
  print("Congratulation! You Won!")
elif player_choice == 1 and computer_choice == 0:
  print("Congratulation! You won!")
else:
  print("Unfortunately, You lost :(")
