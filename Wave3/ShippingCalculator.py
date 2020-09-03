def cost(num):
    if num<1:
        return 0.0
    elif num==1:
        return 10.95
    else:
        return (10.95+(num-1)*2.95)
a = int(input("Please print the number of items purchased "))
print("The total cost is: $"+str(cost(a)))