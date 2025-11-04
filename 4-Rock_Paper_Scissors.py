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
user_selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_selection = random.randint(0,2)
if user_selection >= 0 and user_selection <=2:
    print(game_images[user_selection])
    print(f"Computer chose: \n{game_images[computer_selection]}")

if user_selection == computer_selection:
    print("Draw!")
elif user_selection == 0 and computer_selection == 2:
    print("You Win!")
elif user_selection == 1 and computer_selection == 0:
    print("You Win!")
elif user_selection == 2 and computer_selection == 1:
    print("You Win!")
elif user_selection >= 3 or user_selection < 0:
    print("You typed an invalid number. You Lose!")
else:
    print("You Lose!")
