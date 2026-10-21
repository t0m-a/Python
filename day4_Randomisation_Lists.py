# Randomiser module
import random
import day4_my_module
random_integer = random.randint(1, 10)
print(random_integer)
# This produce a random integer between 1 and 10 (inclusive)
start = 0
stop = 100
step = 3
range(start, stop, step)  
# This is a built-in function that returns a sequence of numbers from start to stop 
# (exclusive) with a step value.
a = 2
b = 5
print(random.uniform(a, b))
print(random.randint(a, b))
print(day4_my_module.my_favourite_number)
# random function of the random module returns a random float number between 0.0 and 1.0 (inclusive of 0.0 but not 1.0).
random_float = random.random() * 100 # shifted by 100 to get a number between 0 and 100
print(random_float)

# List is a data structure. []
# https://docs.python.org/3/tutorial/datastructures.html

# Variables allows to store one value at a time, 
# but lists allow to store multiple values in a single variable. Lists can be ordered.
# They can store mixed data types.
list = ["item1", "item2", "item3"]
fruits = ["Pear", "Apple", "Grapes"]
# Ordered is determined by the position in the list. This is called an index from 0 to first position to position +N
print(fruits[1])
# Position is a shift or offset of the order value. 0 has no offest and is first. Offest +1 is second position. etc.
# minus shift IE: -1 starts selecting from the end of the list.
# Modulate the value of an item stored in a list:
fruits[2] = "Bannana"
print(fruits[2])
print(fruits)
# Add an item to the end of the list .append function:
fruits.append("Pineapple")
print(fruits)
# Add several items .extend Add a list to the original list.
fruits.extend(["Orange", "Apple", "Red Apple"])
print(fruits)
# name_of_the_list.function_applied_to_the_list list_name.append. extend. insert. remove. clear.
print(len(fruits)) # Returns the number of items in a list
# Index out range error working with the total number of items in a list, requires minus shifting by 1 IE:
number_of_fruits = len(fruits) # 7 items
# print(fruits[number_of_fruits]) # Is going to fecth a value in the number of items returned by len. so 7
# The index values runs from 0 to 6 for 7 items, requires shifting the search range by -1 to search from 0 to 6
print(fruits[number_of_fruits -1])

# Nested list, lists within a list
fruits = ["Pear", "Apple", "Grapes"]
vegetables = ["Kale", "Letuce", "Carrot", "Brocoli"]
# 2 different lists, "concatenated" in one list composed of two lists, double [[ brackets at the start and the end]]
fruits_and_vegetables = [fruits, vegetables]
print(fruits_and_vegetables)
# Returns [['Pear', 'Apple', 'Grapes'], ['Kale', 'Letuce', 'Carrot', 'Brocoli']] double[[]] seprated by a comma ,
print(len(fruits_and_vegetables)) # Shows 2 items, 2 lists
print(fruits_and_vegetables[1])
# Fetch items by index number in first list, then second list:
print(fruits_and_vegetables[0][0], fruits_and_vegetables[1][2])