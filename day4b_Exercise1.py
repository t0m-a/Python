import random 
a = random.randint(0, 5)
b = random.randint(6, 10)
result = (random.randint(a, b))
if result == 0 or result <= 5:
    print("Heads")
else:
    print("Tails")