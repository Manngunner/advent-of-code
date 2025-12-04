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


def get_surrounding_score(row: int, column: int, row_max: int, col_max: int) -> int:
    score = 0
    for row_mod, col_mod in DIRECTIONS.values():
        check_row, check_col = row + row_mod, column + col_mod
        # Ensure non-valid indexes are used
        if (check_row < 0 or check_row > row_max) or (check_col < 0 or check_col > col_max):
            continue
        if is_roll(check_row, check_col):
            score += 1
    return score

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
