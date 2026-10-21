# Day 5 Loops in Python and the range() function - Iterating an operation, comparison in Python list of data,
# Using for loops, if statements and operators to build comparisons, values checks  

# The FOR loop:
# for item in list_of_items:
#    do something to each items in the list
fruits = ["apple", "peach", "pear"]
for fruit in fruits:
    print(fruit)
# Runs three times, each time assigning a different value from the list to the variable fruit and performing the function action.
# Then following/looping back to the next value inside the list.
# We execute the same line of code/function several times w/o writing it each time. 
# For as many times/objects or itmes are presents in the list.
fruits = ["apple", "peach", "pear"]
for fruit in fruits: # Fruit is a temporary variable.
    print(fruit) # Re-assigned to each items while the for loop runs in the variable list (fruits)
    print(fruit + " pie")
# Inside for loop VS outside the for loop, based on indentation.
for fruit in fruits:
    print(fruit)
    print(fruits) # happens for as many iterations in the list/loop
# VS outside the loop (at the root leval of identation)
for fruit in fruits:
    print(fruit)
print(fruits) # Happens outside the loop as per the identation level

# Exercise / Example - Python is a number friendly language hence its use for mathematical and data sciences.
scores = [150, 120, 110, 130, 90, 60]
total_scores = sum(scores)
print(total_scores)
# the sum function iterates through the list adding each value to the total amounted by the previous values addition.
# Recreating the sum function with a for loop
# We need a variable to store the previous results of the addition and update it with each iteration.
total_sum = 0
for score in scores:
    total_sum += score # += increment the variable total_sum with each score it is adding through the loop.
print(total_sum)    
# Exercise: recreate the max function which extracts the maximum, greatest value in a list:
print(max(scores))
#
# To get a starting point, we have to assign the variable highest_score and assume the highest score is the first item in the list.
# Define the list
scores = [150, 120, 110, 130, 350, 90, 60, 299]
# Assume the first element is the maximum value of the variable
highest_score = scores[0]
# Loop through each number in the list
for score in scores:
    # If the value is greater than our max value, update the variable max
    if score > highest_score: # Compare the value of the checked score against the highest score value, against the next score in the list.
        highest_score = score
print(highest_score)
print(f"The highest value is: {highest_score}")
# Core concepts: if statement to build the comparison, use of operators to give the comparison type or operation we want to do.
# Use of a defined, not temporary, variable to store the temporary content/result/value of the operation.
# Use the comparison to update the variable content only if (operation result matches), then print the result of the iterated operation.

# for loops and the range() function
