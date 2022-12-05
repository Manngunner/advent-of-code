import re
from collections import deque

with open ("Day 5/input.txt", "r", encoding="utf8") as inputfile:
    inputtext = inputfile.readlines()
    # Make the cargobed first
    for line in inputtext:
        if re.match(r"[\d\s]", line.rstrip()):
            bedlength = re.findall(r"\s+(\d)", line.rstrip())
            cargobed = [deque() for x in bedlength]
            break
    
    # Load the cargobed
    for line in inputtext:
        if re.match(r"[\[\]A-Z]", line.rstrip()):
            cargo = re.findall(r".{3}\s{0,1}", line.rstrip())
            for i in range(len(cargobed)):
                justletter = re.match(r".*([A-Z]).*", cargo[i])
                if justletter:
                    cargobed[i].appendleft(justletter.group(1))

    # Move the shit around
    for line in inputtext:
        moveline = re.match(r"move\s(\d+)\sfrom\s(\d+)\sto\s(\d+)", line.rstrip())
        if moveline:
            quantity = int(moveline.group(1))
            frompos = int(moveline.group(2)) - 1
            topos = int(moveline.group(3)) - 1
            sortdeque = deque()
            for crate in range(quantity):
                sortdeque.append(cargobed[frompos].pop())
            for crate in range(len(sortdeque)):
                cargobed[topos].append(sortdeque.pop())

    # Find the final element
    finalresult = str()
    for stack in cargobed:
        finalresult += stack.pop()
    print(finalresult)