from collections import deque

PRIORITY = '#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

with open ("Day 3/input.txt", "r", encoding="utf8") as inputfile:
    totalpriorities = int()
    badgetype = []
    elfgroup = deque(maxlen=3)
    for line in inputfile.readlines():
        try:
            elfgroup.insert(0, set(line.rstrip()))
        except IndexError:
            badgetype.append(set(elfgroup[0]).intersection(elfgroup[1], elfgroup[2]))
            elfgroup.clear()
            elfgroup.append(set(line.rstrip()))
    badgetype.append(set(elfgroup[0]).intersection(elfgroup[1], elfgroup[2]))

    for itemtype in badgetype:
        totalpriorities += PRIORITY.index(next(iter(itemtype)))
    print(totalpriorities)
