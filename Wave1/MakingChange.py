cent = int(input("Please print how much money the shopper paid in cents"))
if cent == 0:
    print("No Change required")
else:
    print("Change required")
    if cent/200 >= 1 and cent != 0:
        n = int(cent/200)
        print(n, " toonies")
        cent = cent-n*200
    if cent/100 >= 1 and cent != 0:
        n = int(cent/100)
        print(n, " loonies")
        cent = cent- n*100
    if cent/25 >= 1 and cent != 0:
        n = int(cent/25)
        print(n, " quarters")
        cent = cent- n*25
    if cent/10 >= 1 and cent != 0:
        n = int(cent/10)
        print(n, " dimes")
        cent =cent- n*10
    if cent/5 >= 1 and cent != 0:
        n = int(cent/5)
        print(n, " nickels")
        cent =cent- n*5
    if cent != 0:
        print(cent," pennies")
