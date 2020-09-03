a = int(input("Enter an integer (2 or greater): "))
if a<2:
    print("Number is less than 2")
else:
    print("The prime factors of",a,"are: ")
    factor =2
    while factor <=a:
        if a%factor==0:
            print(factor)
            a=a//factor
        else:
            factor+=1
