def reverseLookup(d, val):
    List = []
    for x in d:
        if d[x]==val:
            List.append(x)
    return List
dictionary = {
    "apples":2,
    "pears":2,
    "peaches":1,
    "plums":0
}
print(reverseLookup(dictionary,2)) #this should output 2 keys
print(reverseLookup(dictionary,1)) #this should output 1 key
print(reverseLookup(dictionary,-1)) #this should output no keys
