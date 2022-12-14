import re

with open("Day 4/input.txt", "r", encoding="utf8") as inputfile:
    overlapcount = int()
    linecount = int()
    for line in inputfile.readlines():
        linecount += 1
        cleaning = re.match(r"(\d+)-(\d+),(\d+)-(\d+)", line.rstrip())
        # Gotta convert to int as string comparisons are silly :(
        # Elf 1 range
        elf1low = int(cleaning.group(1))
        elf1high = int(cleaning.group(2))
        # Elf 2 range
        elf2low = int(cleaning.group(3))
        elf2high = int(cleaning.group(4))
        # Apparently if both sets contain the other this still counts :(
        #if elf1low == elf2low and elf1high == elf2high:
        #    continue
        if elf2low >= elf1low and elf2high <= elf1high:
            overlapcount += 1
            continue
        if elf1low >= elf2low and elf1high <= elf2high:
            overlapcount += 1
            continue
    print(overlapcount)
