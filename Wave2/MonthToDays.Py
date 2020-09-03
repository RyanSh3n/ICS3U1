m = input("Please print the month ")
m=m.upper()
if m=="JANUARY"or m=="MARCH"or m=="MAY"or m=="JULY"or m=="AUGUST"or m=="OCTOBER"or m=="DECEMBER":
    print("31 days")
elif m=="APRIL" or m=="JUNE"or m=="SEPTEMBER"or m=="NOVEMBER":
    print("30 days")
else:
    print("28 or 29 days")