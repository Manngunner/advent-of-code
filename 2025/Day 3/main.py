from pathlib import Path

with Path("2025/Day 3/input.txt").open("r") as file:
    banks: list[str] = file.read().strip().split("\n")


total_joltage = 0
for batteries in banks:
    largest_combo = [0, 0]
    for battery in batteries:
        if int(f"{largest_combo[1]}{battery}") > int(f"{largest_combo[0]}{largest_combo[1]}"):
            largest_combo.pop(0)
            largest_combo.append(int(battery))
        if int(f"{largest_combo[0]}{battery}") > int(f"{largest_combo[0]}{largest_combo[1]}"):
            largest_combo.pop()
            largest_combo.append(int(battery))
    total_joltage += int(f"{largest_combo[0]}{largest_combo[1]}")

print(total_joltage)

total_joltage_2 = 0
for batteries in banks:
    largest_combo = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for battery in batteries:
        if f"{''.join(map(str, largest_combo[1:]))}{battery}" > "".join(map(str, largest_combo)):
            largest_combo.pop(0)
            largest_combo.append(int(battery))
            continue
        candidates: list[int] = []
        for index, _ in enumerate(largest_combo):
            test_combo = largest_combo.copy()
            test_combo.pop(index)
            test_combo.append(int(battery))
            candidates.append(int("".join(map(str, test_combo))))
        biggest_combo = str(max(candidates))
        if biggest_combo > "".join(map(str, largest_combo)):
            largest_combo = [int(digit) for digit in biggest_combo]

    total_joltage_2 += int("".join(map(str, largest_combo)))

print(total_joltage_2)
