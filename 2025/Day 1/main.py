from pathlib import Path

with Path("2025/Day 1/input.txt").open("r") as file:
    standard_input: list[str] = file.read().strip().split("\n")

POSITION_MIN = 0
POSITION_MAX = 99
current_position = 50
total_zeros = 0
total_zero_clicks = 0

for movement in standard_input:
    direction: str = movement[0]
    distance: int = int(movement[1:])
    pass_throughs = (distance - distance % 100) // 100
    remainder = distance % 100

    new_position = current_position - remainder if direction == "L" else current_position + remainder
    if new_position < POSITION_MIN:
        new_position = new_position + 100
        if current_position != 0 and new_position != 0:
            pass_throughs += 1
    elif new_position > POSITION_MAX:
        new_position = new_position - 100
        if current_position != 0 and new_position != 0:
            pass_throughs += 1
    if new_position == 0:
        total_zeros += 1
        pass_throughs += 1

    total_zero_clicks += pass_throughs
    current_position = new_position

print(total_zeros)
print(total_zero_clicks)
