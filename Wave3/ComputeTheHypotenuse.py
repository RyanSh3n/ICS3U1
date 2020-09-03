import math
def pythagorean(a, b):
    c = math.pow(a, 2) +math.pow(b, 2)
    return math.sqrt(c)
a = int(input("Please print the first side length "))
b = int(input("Please print the second side length "))
print(pythagorean(a,b))