import random

# import re
# import re not used here as r"""RAW STRING """" does a better job at escaping all special characters in the multiple lines
# written/formatted variables in ASCII art below.
# re would require to write the variable different lines on one line with a \n new line 
# multi_line_str = """Hello!
# How are you?
# Path: C:\\test $100"""
# escaped_str = re.escape(multi_line_str)
# print(escaped_str) 

jack = r"""
.-----------.
| J         |
|   .---.   |
|  /     \  |
|  | ^ ^ |  |
|  |  -  |  |
|  \ 'V' /  |
|   `---'   |
|         J |
`-----------'
"""
queen = r"""
.-----------.
| Q         |
|   _ O _   |
|  ( / \ )  |
|   |v v|   |
|   \_O_/   |
|    _|_    |
|   (   )   |
|         Q |
`-----------'
"""
king = r"""
.-----------.
| K         |
|   _---_   |
|  [M_M_M]  |
|   |o_o|   |
|   \_-_/   |
|   / | \   |
|  /  |  \  |
|         K |
`-----------'
"""
ace = r"""
.-----------.
| A         |
|           |
|     _     |
|    ( )    |
|   (_._)   |
|     |     |
|           |
|         A |
`-----------'
"""

game_images = [jack, queen, king, ace]

user_choice = int(input (f"Choose a card: 0 for the Jack, 1 for the Queen, 2 for the King and 3 for the Ace.\n"))
if user_choice >= 0 and user_choice <= 3:
# if 0 >= user_choice <= 3: # Shorthand variable comparison doesn't print in print(game_images[user_choice]) - Find why.
    print(game_images[user_choice])

# Generate computer's turn random choice    
computer_choice = random.randint(0, 3)
print("Computer chose: \n")
print(game_images[computer_choice])

# Game logic: 3 (the Ace) wins all, 2 (the King) wins 1 (the Queen) and 0 (the Jack), 1 (the Queen) wins 0 (the Jack), 
# 0 (the Jack) looses against all the other cards.
# If the user enters a wrong number, they loose automatically.

if user_choice < 0 or user_choice > 3:
    print("Wrong value, you loose!")
elif computer_choice == 3 and user_choice == 3:
    print("It's a draw!")
elif computer_choice == 3 and user_choice < 3:
    print("You loose!")
elif user_choice == 3 and computer_choice < 3:
    print("You win!")
elif user_choice == 2 and computer_choice == 2:
    print("It's a draw!")
elif user_choice == 2 and computer_choice < 2:
    print("You win!")
elif computer_choice == 2 and user_choice < 2:
    print("You loose!")
elif user_choice == 1 and computer_choice == 1:
     print("It's a draw!")
elif user_choice == 1 and computer_choice < 1:   
    print("You win!!")
elif computer_choice == 1 and user_choice <1 :
    print("You loose.")
elif user_choice == 0 and computer_choice == 0:
    print("It's a draw!")
elif user_choice == 0 and computer_choice < 0:
    print("You loose!")