import random

Names = input("Enter your names separated by commas: ")
N = Names.split(",")
l = len(N)
r = random.randint(0, l-1)
print(N)
print(f"{N[r]} will pay the bill")