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
