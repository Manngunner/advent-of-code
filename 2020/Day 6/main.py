from pathlib import Path

with Path("2020/Day 6/sample").open("r") as file:
    file_parse: list[str] = file.read().strip().split("\n\n")
    sample_input: list[str] = [group.split("\n") for group in file_parse]
with Path("2020/Day 6/input").open("r") as file:
    file_parse: list[str] = file.read().strip().split("\n\n")
    standard_input: list[str] = [group.split("\n") for group in file_parse]


def main(groups: list[list[str]]) -> tuple[int]:
    total = 0
    for group in groups:
        forms = (set(x) for x in group)
        yeses = set.union(*forms)
        total += len(yeses)

    return (total, 2)


if __name__ == "__main__":
    sample = main(sample_input)
    standard = main(standard_input)
print(f"Sample Task 1: {sample[0]}, Sample Task 2: {sample[1]}")
print(f"Actual Task 1: {standard[0]}, Actual Task 2: {standard[1]}")
