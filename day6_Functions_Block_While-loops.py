# Advanced Python functions lessons, code blocks (identation) and while loops.
# Python built-in functions library:
# https://docs.python.org/3/builtins/functions.html
# As lists are defined and recognizable being followed by []
# Functions are defined and recognizable by being followed by ()
# Creating a function starts with def to define it.
# IE definining a function:
def say_hello_and_bye():
    # Everything that comes after the (): and is indented is part of the function.
    print("Hello")
    print("Bye")
    # Do this
    # Then do this
    # Finally do this
# As always the indentation is critical, syntaxical.
# This above is just defining a function ahead of time.
# Calling the function to execute it:
say_hello_and_bye() # Doesn't require an input BTW.
# Writing a function that calls other function(s)
def say_hello_and_bye_twice():
    say_hello_and_bye()
    say_hello_and_bye()
say_hello_and_bye_twice()    
# Simple example using reeborg.ca reeborg's world
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# ​Can do the same the other way around using the turn_right() function we built.
# Using built-in turn_left made more sense to achieve the goal as it was shorter and simpler:
# def walk_in_square():
#     move()        OR turn_left()
#     turn_left()   then move()
#     move()        then turn_right()
#     turn_left()   then move()
#     move()        then turn_right()
#     turn_left()   then move()
#     move()        then turn_right()
#                   then finally move()
# walk_in_square()
#
# First lesson exercise, the hurdle 1 challenge:
# Adding useful turn_right() function sparing code in the next steps
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# Defining the hurdle jump process as a function
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
# Execute defined function jump() using a loop, think sparing code as much as possible.
# Here a for loop running in a range spares writing/running jump() 6 times
# for step in range(6):
#   jump()
#
# While lopp
# Reminder, we saw:
# for item in list_of_items:
#   do something
# This will iterate trhough the whole list content performing an action fir each item in the list.
# for item in range(a, b)
#   do something
# This will peform an action accordingly to the number of times we ask it to do so using a range(), 
# Non-inclusively of the upper top value in the range, so range(1, 6) will iterate the action 5 times.
#
# while something_is_true: # A condition being true:
#   # do domething repeatedly 
a = 10
while a > 0:
    print(a)
    a -= 1
print(f"Done: a = {a}.")
# In the previous exercise we defined functions turn_right() and jump()
# Running the functions until we arrive at_goal(), being unpredictable.
# while at_goal() == False: 
# Or not equal to True ** != True **
# Or while not at_goal():
#    jump()
# ** We can use a function as a condition to evaluate ** as True or False in a while loop. /!\
a = 0
def our_target():
    return a == 23
while not our_target():
    a += 1
print(f"We're done, our target returns expected value: {a}\n")
print("Another method is declaring != (not) True")
while our_target() != True:
    a += 3
print(f"We're done, our target is not NOT True anymore: {a}\n")
# Or == False, while the condition is still strictly False.
#
# Main conceptual difference between using FOR or WHILE loops:
# FOR loops are good to iterate an action over each pass until the steps, passes are completed, 
# IE: Iterating through a complete list doing something to/with each item.
# Where a WHILE loop is great when you need to perform an action through multiple steps 
# But then only do something when iterations reach a specific expected result, a condition change being validated,
# Whether you want it to result in being False at some point or being True at some point. While not caring about the 
# intermediate states until the condition validation to get out of the loop has been reached.
#
# /!\ Be aware of misprogramming a condition in the while loop will provoke an infite loop. /!\
# If you don't understand while you've hit an infinite loop, print out your condition in the loop(s).
# This way you can see where and which condition is stucking the code in a loop, IE:
# while 5 == 5:
#   print while 5 == 5
#   jump()
# Will print True all the times, in the part of the code the condition is misprogrammed.
#
# Second exercise, nesting multiple conditions checks in one while loop:
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# A condition being or switching to True is an IMPLICT in the while loop.  
# Declaring condition == True: is redundant below. The second method I used shows this.
# If NOT True do something, if True move on to the next step(s).
#
# while not at_goal():
#     if front_is_clear() == True:
#         move()
#     elif wall_in_front() == True:
#         jump()
#
# A better manner to express the conditions' statuses verification:
# while not at_goal():
#     if not wall_in_front():
#         move()
#     elif not front_is_clear():
#         jump()
# Better and shorter:
# while not at_goal():
#     if wall_in_front(): # Implicit True if not True move on to the next.
#       jump()
#     else:
#       move()