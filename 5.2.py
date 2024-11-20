import pytest


def contains_pairs(input):

    return False


def contains_triple(input):
    return False


def main(input):
    return contains_pairs(input) or contains_triple(input)


# Tests
print("testing: contains_pairs")
for (input, expected) in [("xyxy", True),
                          ("xaabcdefgaa", True),
                          ("xsaaasx", False)]:
    print(f"  {input} : {contains_pairs(input) == expected}")
