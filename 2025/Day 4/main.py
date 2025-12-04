from pathlib import Path

with Path("2025/Day 4/input.txt").open("r") as file:
    tmp: list[str] = file.read().strip().split("\n")
    department: list[list[str]] = [list(space) for space in tmp]

DIRECTIONS = {
    "left": (0, -1),
    "right": (0, +1),
    "up": (-1, 0),
    "down": (+1, 0),
    "left_up": (-1, -1),
    "right_up": (-1, +1),
    "left_down": (+1, -1),
    "right_down": (+1, +1),
}
MAX_ROLLS = 3


def is_roll(row: int, column: int) -> bool:
    return department[row][column] == "@"


def get_surrounding_score(row: int, column: int, row_max_index: int, column_max_index: int) -> int:
    look_up = row != 0
    look_down = row != row_max_index
    look_left = column != 0
    look_right = column != column_max_index
    surrounding_score = 0
    if look_up and look_down and look_left and look_right:
        for direction in DIRECTIONS:  # noqa: PLC0206
            row_mod, col_mod = DIRECTIONS[direction]
            if is_roll(row + row_mod, column + col_mod):
                surrounding_score += 1
    if not look_up:
        for direction in ["left", "right", "down", "left_down", "right_down"]:
            row_mod, col_mod = DIRECTIONS[direction]
            if is_roll(row + row_mod, column + col_mod):
                surrounding_score += 1
    if not look_down:
        for direction in ["left", "right", "up", "left_up", "right_up"]:
            row_mod, col_mod = DIRECTIONS[direction]
            if is_roll(row + row_mod, column + col_mod):
                surrounding_score += 1
    if not look_left:
        for direction in ["right", "up", "down", "right_up", "right_down"]:
            row_mod, col_mod = DIRECTIONS[direction]
            if is_roll(row + row_mod, column + col_mod):
                surrounding_score += 1
    if not look_right:
        for direction in ["left", "up", "down", "left_up", "left_down"]:
            row_mod, col_mod = DIRECTIONS[direction]
            if is_roll(row + row_mod, column + col_mod):
                surrounding_score += 1

    return surrounding_score


removeable_indexes: list[tuple[int, int]] = []
total_removed: int = 0


def main() -> int:
    accessible_rolls = 0
    column_max_index = len(department) - 1
    for row_index, row in enumerate(department):
        row_max_index = len(row) - 1
        for column_index, _ in enumerate(row):
            # Check for corner spot
            if not is_roll(row_index, column_index):
                continue
            if (row_index in (0, row_max_index)) and (column_index in (0, column_max_index)):
                accessible_rolls += 1
                removeable_indexes.append((row_index, column_index))
                continue
            if get_surrounding_score(row_index, column_index, row_max_index, column_max_index) <= MAX_ROLLS:
                accessible_rolls += 1
                removeable_indexes.append((row_index, column_index))
    return accessible_rolls


print(main())

while len(removeable_indexes) > 0:
    for roll in removeable_indexes:
        department[roll[0]][roll[1]] = "."
    total_removed += len(removeable_indexes)
    removeable_indexes.clear()
    main()

print(total_removed)
