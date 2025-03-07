import math
from pathlib import Path

with Path("2020/Day 3/sample").open("r") as file:
    sample_input: list[str] = file.read().strip().split("\n")
with Path("2020/Day 3/input").open("r") as file:
    standard_input: list[str] = file.read().strip().split("\n")


def main(course: list[str]) -> tuple[int]:
    course_width: int = len(course[0]) - 1
    course_length: int = len(course) - 1

    x_position = [0, 0, 0, 0, 0]
    y_position = [0, 0, 0, 0, 0]
    trees_counted = [0, 0, 0, 0, 0]

    while any(bool(y <= course_length) for y in y_position):
        y_position[0] += 1
        y_position[1] += 1
        y_position[2] += 1
        y_position[3] += 1
        y_position[4] += 2
        x_position[0] += 1
        x_position[1] += 3
        x_position[2] += 5
        x_position[3] += 7
        x_position[4] += 1

        for index, (y, x) in enumerate(zip(y_position, x_position, strict=True)):
            if y > course_length:
                continue
            if x > course_width:
                x_position[index] = x_position[index] - course_width - 1
            if course[y_position[index]][x_position[index]] == "#":
                trees_counted[index] += 1
    return (trees_counted[1], math.prod(trees_counted))


sample = main(sample_input)
standard = main(standard_input)
print(f"Sample Task 1: {sample[0]}, Sample Task 2: {sample[1]}")
print(f"Actual Task 1: {standard[0]}, Actual Task 2: {standard[1]}")
