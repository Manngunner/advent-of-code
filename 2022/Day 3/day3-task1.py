
PRIORITY = '#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

with open("Day 3/input.txt", "r", encoding="utf8") as inputfile:
    totalpriorities = int()
    commontype = []
    for line in inputfile.readlines():
        linesplit = int(len(line.rstrip()) / 2)
        compartment1 = line[:linesplit].rstrip()
        compartment2 = line[linesplit:].rstrip()
        commontype.append(next(iter(set(compartment1).intersection(compartment2))))

    for itemtype in commontype:
        totalpriorities += PRIORITY.index(itemtype)
    print(totalpriorities)
