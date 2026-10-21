import random
# First method using what I already knew
friends = ["Alice", "Bob", "Charly", "Emma"]
random_friend = random.randint(0, 3)
print(friends[random_friend])

# Second method using choice function
random_friend_2 = random.choice(friends)
print(random_friend_2)
# Shorter way
print(random.choice(friends))