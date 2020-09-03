days = int(input("Please print the number of days "))
hours = int(input("Please print the number of hours "))
minutes = int(input("Please print the number of minutes "))
seconds = int(input("Please print the number of seconds "))
tot = days*24*60*60+hours*60*60+minutes*60+seconds
print("The total number of seconds in this duration is", tot)