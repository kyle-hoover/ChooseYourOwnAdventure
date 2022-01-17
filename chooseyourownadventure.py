print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to Treasure Island. \nYour mission is to find the treasure.")

first_choice = input("You come to a fork in the road. Will you go left or right (left or right)? ")

if first_choice.lower() != "left":
    print("You fell into a hole. Game over.")
else:
    second_choice = input("You come to a river. Will you choose to swim or wait for a boat (swim or wait)? ")
    if second_choice.lower() != "wait":
        print("You were attacked by a shark. Game over")
    else:
        third_choice = input("You come across 3 doors. Red, yellow and blue. Which will you enter (red, yellow or blue)? ")
        if third_choice.lower() == "blue":
            print("You were eaten by beasts. Game over.")
        elif third_choice.lower() == "red":
            print("You were burned by fire. Game over.")
        elif third_choice.lower() == "yellow":
            print("You found the treasure! You win!")
        else:
            print("You did not choose a door. Game over.")
