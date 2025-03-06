from itertools import product
from pathlib import Path

TARGET = 2020

with Path("2020/Day 1/sample").open("r") as file:
    sample_input: list[int] = [int(line) for line in file.read().strip().split("\n")]
    sample_input.sort()
with Path("2020/Day 1/input").open("r") as file:
    standard_input: list[int] = [int(line) for line in file.read().strip().split("\n")]
    standard_input.sort()


def main(bills: list[int]) -> tuple[int] | None:
    two_biggest_int = 2021 - bills[0]
    three_biggest_int = 2021 - bills[0] + bills[1]
    two_multiplied = 0
    three_multiplied = 0

    for first, second, third in product(bills, bills, bills):
        if first >= two_biggest_int or second >= two_biggest_int:
            continue
        if first + second == TARGET or two_multiplied:
            two_multiplied = first * second
        if first >= three_biggest_int or second >= three_biggest_int or third >= three_biggest_int:
            continue
        if first + second + third == TARGET:
            three_multiplied = first * second * third
        if two_multiplied and three_multiplied:
            return (two_multiplied, three_multiplied)
    return None

sample = main(sample_input)
standard = main(standard_input)
print(f"Sample Task 1: {sample[0]}, Sample Task 2: {sample[1]}")
print(f"Actual Task 1: {standard[0]}, Actual Task 2: {standard[1]}")
