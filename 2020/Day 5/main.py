from pathlib import Path

with Path("2020/Day 5/sample").open("r") as file:
    sample_input: list[str] = file.read().strip().split("\n")
with Path("2020/Day 5/input").open("r") as file:
    standard_input: list[str] = file.read().strip().split("\n")


def main(seats: list[str]) -> tuple[int]:
    highest_score: int = 0
    all_scores: list[int] = []
    your_seat: int = 0
    for row in seats:
        seat_rows = [*range(128)]
        seat_columns = [*range(8)]
        current_row = 128
        current_column = 8
        for position in row:
            if current_row == 1:
                if position == "L":
                    current_column = int(current_column / 2)
                    del seat_columns[current_column:]
                if position == "R":
                    current_column = int(current_column / 2)
                    del seat_columns[:current_column]
            if position == "F":
                current_row = int(current_row / 2)
                del seat_rows[current_row:]
            if position == "B":
                current_row = int(current_row / 2)
                del seat_rows[:current_row]
        current_score = seat_rows[0] * 8 + seat_columns[0]
        all_scores.append(current_score)
        highest_score = max(highest_score, current_score)
    all_scores.sort()
    for index, seat in enumerate(all_scores, 81):
        if index != seat:
            your_seat = seat - 1
            break
    return (highest_score, your_seat)


if __name__ == "__main__":
    sample = main(sample_input)
    standard = main(standard_input)
print(f"Sample Task 1: {sample[0]}, Sample Task 2: {sample[1]}")
print(f"Actual Task 1: {standard[0]}, Actual Task 2: {standard[1]}")
