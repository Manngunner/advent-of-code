import re
from collections import deque

with open("Day 1/input.txt", "r") as inputfile:
    calories = int()
    counter = int()
    topthreecalories = deque([1, 2, 3], maxlen=3)
    for line in inputfile.readlines():
        if re.match("\d+", line):
            calories += int(line)
            continue
        for entry in topthreecalories:
            if calories > entry:
                try:
                    topthreecalories.insert(counter, calories)
                except IndexError:
                    topthreecalories.pop()
                    topthreecalories.insert(counter, calories)
                finally:
                    break
            counter = counter + 1
        calories = int()
        counter = int()
    print(sum(topthreecalories))
