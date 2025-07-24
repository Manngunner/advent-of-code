import re
from pathlib import Path

with Path("Day 7/sample").open("r") as file:
    sample_input: list[str] = file.read().strip().split("\n")
with Path("Day 7/input").open("r") as file:
    standard_input: list[str] = file.read().strip().split("\n")

MATCHING_BAG = "shiny gold"
RULE_REGEX = re.compile(r"([a-z\s]+)\sbags\scontain\s(.*)")
CONTENT_REGEX = re.compile(r"\s?(\d+|no)\s([a-z\s]+)")


def main(rules: list[str]) -> tuple[int, str]:
    bags_with_gold: set[str] = set()
    count_previous = -1
    count_new = 0

    while len(bags_with_gold) > count_previous:
        for rule in rules:
            rule_parse = RULE_REGEX.search(rule)
            if not rule_parse:
                continue
            rule_bag = rule_parse.group(1)
            rule_contents = [CONTENT_REGEX.search(bag) for bag in rule_parse.group(2).split(",")]

            for bag in rule_contents:
                if not bag:
                    continue
                if bag.group(2).find(MATCHING_BAG) != -1:
                    bags_with_gold.add(rule_bag)
                for bag_with_gold in list(bags_with_gold):
                    if bag.group(2).find(bag_with_gold) != -1:
                        bags_with_gold.add(rule_bag)

        count_previous = count_new
        count_new = len(bags_with_gold)

    return (len(bags_with_gold), "2")


# dotted turquoise bags contain 2 shiny green bags, 5 striped magenta bags, 3 muted green bags.

if __name__ == "__main__":
    sample = main(sample_input)
    standard = main(standard_input)
    print(f"Sample Task 1: {sample[0]}, Sample Task 2: {sample[1]}")
    print(f"Actual Task 1: {standard[0]}, Actual Task 2: {standard[1]}")
