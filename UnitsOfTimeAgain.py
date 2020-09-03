seconds = int(input("Please print the number of seconds "))
days = int(seconds/86400)
seconds = seconds%86400
hours =int(seconds/3600)
seconds = seconds%3600
minutes =int(seconds/60)
seconds = seconds%60
print('%.1d:%.2d:%.2d:%.2d' % (days, hours, minutes, seconds))

    