import random

# Defining lists of characters useable for user inputs and password creation.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# UI starting the password generator and prompting for user inputs defining number of characters by type.
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Defining and initializing empty variables used to store random charaters generations and choices.
password = ""
letters_in_password = ""
numbers_in_password = ""
symbols_in_password = ""

# Generating random letters selection and truncating to user's input value.
for letter in letters:
    letters_in_password += random.choice(letters)
truncated_letters_in_password = letters_in_password[:nr_letters]
# print(truncated_letters_in_password)
#
# Alternative method to generate random strings using range(), as in the exercise provided solution:
# password = ""
# Enumerate characters chars in a range from 1 to the number of letters chosen by the user adding +1 at the end 
# to include the last letter/characters/item of the range, see range() function in course notes. 
# IE: 4 characters request with range from 1 to 5 generating a character at each pass of the range.
# Remeber range() doesn't include the upper limit.
# for chars in range(1, nr_letters + 1):
#   Making a random.choice in the list of letters and storing the result in a variable
#   random_chars = random.choice(letters)
#   Concatenating the random characters in a string and adding it to the password variable
#   password += random_chars
# Shorter version
# for chars in range(1, nr_letters, 1):
#   password =+ random.choice(letters)
# Even shorter, iterate the for loop below with nr_symbols using list symbols and nr_numbers using list numbers. 
# for chars in range(0, nr_letters):
#   password =+ random.choice(letters)
# Then to randomize the final results into the final password, use a list for password variable rather then a string.
# password_list = []
# for chars in range(0, nr_letters):
#  Adding results or append results to the passowrd_list object.
#   password_list =+ random.choice(letters)
#OR password_list.append(random.choice(letters))
# Then randomizing the content of the list passowrd_list.
# random.shuffle(password_list)
# Then retreiving the shuffled content of passowrd_list and storing/converting the content into a string:
# Initializing an empty string for the final password
# password = ""
# Iterating through the list and adding each character into the string
# for char in passowrd_list:
# password += char

# Generating random symbols selection and truncating to user's input value.
for symbol in symbols:
    symbols_in_password += random.choice(symbols)
truncated_symbols_in_password = symbols_in_password[:nr_symbols]
# print(truncated_symbols_in_password)

# Generating random numbers selection and truncating to user's input value.
for number in numbers:
    numbers_in_password += random.choice(numbers)
truncated_numbers_in_password = numbers_in_password[:nr_numbers]
# print(truncated_numbers_in_password)

# Randomizing generated results as per inputted user's limits, into a final password string.
# Then displaying the final result to the user
# Concatenate values of truncated_* variables, with "" it's combining the literal text, 
# the variables names, not their inner value. Write it with parenthesis to be able to write all
# the variables called on different lines, it makes the block of code cleaner to read than 
# a one line of code and represents better that it is a function you created (concatenation).
randomizing_password = (
    truncated_letters_in_password 
    + truncated_numbers_in_password 
    + truncated_symbols_in_password
)
# randomizing_password is a string, to shuffle it it requires to be converted a mutable element,
# like a list. Using the list function on the randomizing_password variable and storing it in a new variables
# Converting the string to a list
password_chars = list(randomizing_password)
# Shuffle the list
random.shuffle(password_chars)
# Random shuffle needs a mutable sequence such as a list, a string is not mutable in place, as is,
# It is a fixed sequence.
# Join back the shuffle list content as a string
password = "".join(password_chars)
print(f"Your generated password is:\n {password}")