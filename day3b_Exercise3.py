print("Welcome to Treaure Island.\n Your mission is to find the treasure.")
user_name = input("What is your name?\n")
print(f"Welcome, {user_name}!")
choice1 = input(f'{user_name}, you are at a cross road. Where do you want to go? Type "left" or "right"\n').lower()
if choice1 == "left":
    choice2 = input(f'You have come to a lake. Choose wisely, {user_name}, there is an island in the middle of the lake.'
                    f'Type "wait" to wait for a boat.' 
                    'Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue." 
                        "Which color do you choose?\n").lower()
        if choice3 == "red":
            print(f"Sorry, {user_name}. It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print(f"Congratulations, {user_name}! You found the treasure! You Win!")
        elif choice3 == "blue":
            print(f"Sorry, {user_name}. You enter a room of beasts. Game Over.")
        else:
            print(f"Sorry, {user_name}. You chose a door that doesn't exist. Game Over.")
    else:
        print(f"Sorry, {user_name}. You get attacked by an angry trout. Game Over.")