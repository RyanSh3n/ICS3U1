pos = input("Please print the position ")
arr = list(pos)
p2 = arr[0]
p1 = int(arr[1])
if p1==1 or p1==3 or p1==5 or p1==7:
    if p2=='a' or p2=='c' or p2=='e' or p2=='g':
        print("The square is black")
    else:
        print("The squares is white")
else:
    if p2=='a' or p2=='c' or p2=='e' or p2=='g':
        print("The square is white")
    else: 
        print("The square is black")
