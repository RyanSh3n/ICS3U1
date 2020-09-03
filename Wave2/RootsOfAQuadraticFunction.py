import math
a = int(input("Please print the a value "))
b = int(input("Please print the b value "))
c = int(input("Please print the c value "))
numr = b*b-(4*a*c)
if numr<0:
    print("No real roots")
elif numr==0:
    print("One real root")
    root = -1*b/2*a
    print(root)
else:
    print("Two real roots")
    r1 = (-1*b+math.sqrt(numr))/2*a
    r2 = (-1*b-math.sqrt(numr))/2*a
    print("Root one is ", r1)
    print("Root two is ", r2)


