from pathlib import Path


def find_basement(input):
    floor = 0
    index = 0
    for c in input:
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
        if floor < 0:
            return index + 1
        index += 1


print(f"example 1: {find_basement(')') == 1}")
print(f"example 2: {find_basement('()())') == 5}")

input = Path("./inputs/1.txt").read_text()
print(f"answer: {find_basement(input)}")
