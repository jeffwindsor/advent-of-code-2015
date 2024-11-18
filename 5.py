def parse(file):
    with open(file, "r") as file:
        return (line.strip() for line in file.readlines())

def is_nice1(string):
    # Rule 1: At least three vowels
    vowels = "aeiou"
    vowel_count = sum(1 for char in string if char in vowels)

    # Rule 2: At least one double letter
    has_double = any(string[i] == string[i+1] for i in range(len(string) - 1))

    # Rule 3: Does not contain forbidden substrings
    forbidden = ["ab", "cd", "pq", "xy"]
    contains_forbidden = any(sub in string for sub in forbidden)

    # String is nice if all conditions are met
    return vowel_count >= 3 and has_double and not contains_forbidden

def is_nice2(string):
    # Rule 1: Check for a pair that appears at least twice without overlapping
    has_repeated_pair = any(string[i:i+2] in string[i+2:]
                            for i in range(len(string) - 1))

    # Rule 2: Check for a letter repeating with exactly one letter between them
    has_repeat_with_gap = any(string[i] == string[i+2]
                              for i in range(len(string) - 2))

    # A string is nice if both rules are satisfied
    return has_repeated_pair and has_repeat_with_gap

def count_nice_strings(is_nice_func, file):
    return sum((is_nice_func(line) for line in parse(file)))

if __name__ == "__main__":
    print(f"part 1 (236): {count_nice_strings(is_nice1, './inputs/5.txt')}")
    print(f"part 2  (51): {count_nice_strings(is_nice2, './inputs/5.txt')}")
