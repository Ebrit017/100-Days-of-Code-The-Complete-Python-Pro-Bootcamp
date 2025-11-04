print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

option1 = input('You\'re at a stop sign. Where do you want to go?\n'
                '   Type "Left" or "Right"\n').lower()

if option1 == "left":
    option2 = input('You found a lake with a dock and see a mysterious island in the middle. Do you want to wait for a boat or swim?\n'
                    '   Type "Swim" or "Wait"\n').lower()

    if option2 == "wait":
        option3 = input('You made it to the island but see three colored doors. Which door do you want to go through?\n'
                        '   Type "Red", "Yellow", or "Blue"\n').lower()

        if option3 == "red":
            print("You got attacked by skeletons. Game Over.")
        elif option3 == "yellow":
            print("You found the treasure! YOU WIN!")
        elif option3 == "blue":
            print("You fell into a trap hole. Game Over.")
        else:
            print("That door does not exist. Game Over.")
    else:
        print("You got attacked by a shark. Game Over.")
else:
    print("You drove into a dead end. Game Over.")
