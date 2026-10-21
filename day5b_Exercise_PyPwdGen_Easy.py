import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
letters_in_password = ""
numbers_in_password = ""
symbols_in_password = ""

for letter in letters:
    letters_in_password += random.choice(letters)
truncated_letters_in_password = letters_in_password[:nr_letters]
# print(truncated_letters_in_password)

for symbol in symbols:
    symbols_in_password += random.choice(symbols)
truncated_symbols_in_password = symbols_in_password[:nr_symbols]
# print(truncated_symbols_in_password)

for number in numbers:
    numbers_in_password += random.choice(numbers)
truncated_numbers_in_password = numbers_in_password[:nr_numbers]
# print(truncated_numbers_in_password)

password = truncated_letters_in_password + truncated_symbols_in_password +truncated_numbers_in_password 
print(password)