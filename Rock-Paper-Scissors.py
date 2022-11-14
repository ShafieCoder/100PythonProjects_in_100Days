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

#Write your code below this line 👇
# rock (0) wins against scissors (2)
# scissors (2) win against paper (1)
# paper(1) win against rock(0)
import random
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)
if player_choice == 0:
  print(f"player choice:\n {rock}")
elif player_choice == 1:
  print(f"player choice:\n {paper}")
elif player_choice == 2:
  print(f"player choice:\n {scissors}")

if computer_choice == 0:
  print(f" computer choice:\n {rock}")
elif computer_choice == 1:
  print(f"player choice:\n {paper}")

elif computer_choice == 2:
  print(f"player choice:\n {scissors}")


if player_choice == 0 and computer_choice == 2:
  print("Congratulation! You Won!")
elif player_choice == 2 and computer_choice == 1:
  print("Congratulation! You Won!")
elif player_choice == 1 and computer_choice == 0:
  print("Congratulation! You won!")
else:
  print("Unfortunately, You lost :(")
