# Rollercoaster from scratch.
print("Welcome to the rollercoaster!")
print("Please enter your height in cm: ")
height = int(input())

if height >= 160:
    print("You are tall enough to ride the roller coaster!")
    print("Please enter your age: ")
    age = int(input())
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        # elif 45 <= age <= 55: # this is also a valid, shorter, way to write the condition
        bill = 0 # variable already set to 0 at the start of the program, so this is not necessary, 
        # but it is here for clarity.
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    input_photo = input("Do you want a photo taken? Y or N: ")
    if input_photo == "Y":
        bill += 3
        print("Photo price is $3.")
    print(f"Your total bill is ${bill}")

else:
    print("Sorry, you need to be at least 160cm to ride the roller coaster.")