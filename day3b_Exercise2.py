print("Welcome to the ride")
bill = 0
height = int(input("Please enter your height in cm: "))

if height >= 120:
	print("You are tall enough to ride")
	age = int(input("Please enter your age: "))
	if age <= 12:
		bill = 5
		print("Children under 12 pay $5")
	elif age <= 18 and age >= 60:
		bill = 7
		print("Teens and adults pay $7")
	else:
		bill = 4
		print("Seniors pay $4")

	input_photo = input("Do you want a photo taken? yes or no: ")
	if input_photo == "yes":
		bill += 3
		print("Photo price is $3")
	print(f"Your total bill is ${bill}")

else:
	print("Sorry you cannot ride")