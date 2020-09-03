def fun(a):
    check = False
    for x in range(2,a):
        if a%x==0:
            check = True
    if check or a==1:
        return("The number is not a prime")
    else:
        return("The number is a prime")

a = int(input("Please print a number "))
print(fun(a))