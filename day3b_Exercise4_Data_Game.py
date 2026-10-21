import ast

print("Let's play with data")
user_input = input("Please enter desired data: \n")
try:
    # Safely evaluate the input to its native Python type
    parsed_input = ast.literal_eval(user_input)
except (ValueError, SyntaxError):
    # If evaluation fails, it is treated as a plain string
    parsed_input = user_input
print(f"Value: {parsed_input} | Type: {type(parsed_input)}")

data_type = type(parsed_input)
if data_type == str:
    print("You entered a string")
elif data_type == int:
    print("You entered an integer")
elif data_type == float:
    print("You entered a float")
else:
    print(f"You entered data of type {data_type}")

print("Play some more?")
play_again = input("Enter Y for yes, N for no: \n").strip().upper()
if play_again == 'Y':
    print("Let's play again!")
    print("Let's check if the data is numeric")
    if data_type == str and parsed_input.isnumeric():
        print("You entered a numeric string")
    if data_type == int:
        print("You entered a numeric integer")
    if data_type == float:
        print("You entered a numeric float")
    elif data_type == str and not parsed_input.isnumeric():
        print("You did not enter a numeric value")
    elif data_type not in [str, int, float]:
        print("You did not enter a numeric value")    
else:
    print("Thanks for playing! Goodbye!")