import re
from pathlib import Path

with Path("2020/Day 2/sample").open("r") as file:
    sample_input: list[str] = file.read().strip().split("\n")
    sample_input.sort()
with Path("2020/Day 2/input").open("r") as file:
    standard_input: list[str] = file.read().strip().split("\n")
    standard_input.sort()


def main(user_passwords: list[str]) -> tuple[int]:
    count = 0
    correct_passwords = 0

    for user_password in user_passwords:
        password_parse = re.match(r"(\d+)-(\d+)\s*(\w):\s(\w+)", user_password)
        min_char = int(password_parse.group(1))
        max_char = int(password_parse.group(2))
        char = password_parse.group(3)
        password = password_parse.group(4)

        if min_char <= password.count(char) <= max_char:
            count += 1

        first_char = password[min_char - 1]
        last_char = password[max_char - 1]

        if first_char == char and last_char == char:
            continue
        if first_char == char:
            correct_passwords += 1
        if last_char == char:
            correct_passwords += 1
    return (count, correct_passwords)


sample = main(sample_input)
standard = main(standard_input)
print(f"Sample Task 1: {sample[0]}, Sample Task 2: {sample[1]}")
print(f"Actual Task 1: {standard[0]}, Actual Task 2: {standard[1]}")
