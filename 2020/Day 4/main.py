import re
from pathlib import Path

REQUIRED_FIELDS: list[str] = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
VALID_EYE_COLOURS: list[str] = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

with Path("2020/Day 4/sample").open("r") as file:
    file_content: list[str] = file.read().split("\n\n")
    sample_input: list[str] = [line.replace("\n", " ") for line in file_content]
with Path("2020/Day 4/input").open("r") as file:
    file_content: list[str] = file.read().split("\n\n")
    standard_input: list[str] = [line.replace("\n", " ") for line in file_content]


def main(passports: list[str]) -> None:
    count1 = 0
    count2 = 0
    for passport in passports:
        valid1 = True
        valid2 = True
        for field in REQUIRED_FIELDS:
            key_value = re.search(rf"({field}):(\S+)", passport)
            if not key_value:
                valid1 = False
                valid2 = False
                break
            key = key_value.group(1)
            value = key_value.group(2)
            if key == "byr" and not 1920 <= int(value) <= 2002:
                valid2 = False
                continue
            if key == "iyr" and not 2010 <= int(value) <= 2020:
                valid2 = False
                continue
            if key == "eyr" and not 2020 <= int(value) <= 2030:
                valid2 = False
                continue
            if key == "hgt" and not any(
                [
                    bool(value[-2:] == "cm" and 150 <= int(value[:-2]) <= 193),
                    bool(value[-2:] == "in" and 59 <= int(value[:-2]) <= 76),
                ],
            ):
                valid2 = False
                continue
            if key == "hcl" and not re.match(r"#[0-9a-f]{6}$", value):
                valid2 = False
                continue
            if key == "ecl" and value not in VALID_EYE_COLOURS:
                valid2 = False
                continue
            if key == "pid" and not re.match(r"\d{9}$", value):
                valid2 = False
                continue
        if valid1:
            count1 += 1
        if valid2:
            count2 += 1
    return (count1, count2)


if __name__ == "__main__":
    sample = main(sample_input)
    standard = main(standard_input)
print(f"Sample Task 1: {sample[0]}, Sample Task 2: {sample[1]}")
print(f"Actual Task 1: {standard[0]}, Actual Task 2: {standard[1]}")
