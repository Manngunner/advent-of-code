import re
from pathlib import Path

with Path("2025/Day 2/input.txt").open("r") as file:
    standard_input: list[str] = file.read().strip().split(",")

invalid_sum = 0
invalid_sum_2 = 0

for id_range in standard_input:
    products = re.search(r"(\d+)-(\d+)", id_range)

    lower = 0
    upper = 0
    if products:
        lower = int(products.group(1))
        upper = int(products.group(2))

    for product in range(lower, upper+1):
        product_length = len(str(product))
        factors = [
            factor
            for factor in range(1, product_length + 1)
            if product_length % factor == 0 and factor != product_length
        ]

        for factor in factors:
            is_invalid = True
            for i in range(1, int(product_length / factor)):
                if str(product)[0:factor] != str(product)[factor * i : (factor * i) + factor]:
                    is_invalid = False
                    break

            if is_invalid:
                invalid_sum_2 += product
                break

        if product_length % 2 != 0:
            continue
        first_half = str(product)[: int(product_length / 2)]
        second_half = str(product)[int(product_length / 2) :]
        halfway = int(len(str(product)) / 2)

        if first_half == second_half:
            invalid_sum += product

print("### Results ###")
print(invalid_sum)
print(invalid_sum_2)
