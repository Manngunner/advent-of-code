import re

with open("Day 1/input.txt", "r", encoding="utf8") as inputfile:
    calories = int()
    highestcalories = int()
    for line in inputfile.readlines():
        if re.match("\d+", line):
            calories += int(line)
            continue
        if calories > highestcalories:
            highestcalories = calories
        calories = int()
    print(highestcalories)
