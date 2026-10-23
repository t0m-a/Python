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
