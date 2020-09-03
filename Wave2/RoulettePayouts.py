import random
val = random.randint(0, 37)
if val==37:
    print("Pay 00")
elif val == 0:
    print("Pay 0")
else:
    print("The spin resulted in "+str(val)+"...")
    print("Pay",val)
    color = "Black"
    if val==1 or val==3 or val==5 or val==7 or val==9 or val==12 or val==14 or val ==16 or val==18 or val==19 or val==21 or val==23 or val==25 or val==27 or val==30 or val==32 or val==34 or val==36:
        color="Red"
    print("Pay "+color)
    if val%2==0:
        print("Pay Even")
    else:
        print("Pay Odd")
    if val<=18:
        print("Pay 1 to 18")
    else:
        print("Pay 19 to 36")