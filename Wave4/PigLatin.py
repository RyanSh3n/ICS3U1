def Pig (a):
    temp = a
    if a[0]=='a' or a[0]=='e' or a[0]=='i' or a[0]=='o' or a[0]=='u':
        temp+="way"
        return temp
    else:
        v=-1
        temp=""
        for i in range(0,len(a)):
            if a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u':
                v=i
                temp+=a[v:]+a[:v]+"ay"
                return temp

word = input("Please print a line of text ")
word = word.split(" ")
for a in word:
    print(Pig(a))