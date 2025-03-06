from collections import Counter

with open("Day 6/input.txt", "r", encoding="utf8") as inputfile:
    encodedstring = inputfile.readline()
    markersize = 4
    for i in range(len(encodedstring.rstrip())):
        if len(Counter(encodedstring[i:i+markersize].rstrip())) == markersize:
            print(i+markersize)
            break