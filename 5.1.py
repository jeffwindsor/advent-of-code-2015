vowels = ['a', 'e', 'i', 'o', 'u']


def isVowel(char):
    return (char in vowels)


def containsAtLeastThreeVowels(input):
    count = 0
    for c in input:
        if isVowel(c):
            # print(f"{c} at {count}")
            count += 1
            if count >= 3:
                return True
    return False


def containsNaughtyPhrase(input):
    return (
        (input.find('ab') != -1) or
        (input.find('cd') != -1) or
        (input.find('pq') != -1) or
        (input.find('xy') != -1)
    )


def containsDoubleLetter(input):
    last = ''
    for current in input:
        if current == last:
            return True
        last = current
    return False


def isNiceString(input):
    return (
        containsAtLeastThreeVowels(input) and
        (not containsNaughtyPhrase(input)) and
        containsDoubleLetter(input)
    )


def main(input):
    return isNiceString(input)


print("Day 5: Doesn't He Have Intern-Elves For This?")
print()

print("Tests")

print(f"Rule containsNaughtyPhrase: ab is {containsNaughtyPhrase('.ab.')}")
print(f"Rule containsNaughtyPhrase: cd is {containsNaughtyPhrase('.cd.')}")
print(f"Rule containsNaughtyPhrase: pq is {containsNaughtyPhrase('.pq.')}")
print(f"Rule containsNaughtyPhrase: xy is {containsNaughtyPhrase('.xy.')}")
print(
    f"Rule NOT containsNaughtyPhrase: asdf is {not containsNaughtyPhrase('.asdf.')}")

print(f"Rule containsDoubleLetter: xx is {containsDoubleLetter('.aa.')}")
print(
    f"Rule NOT containsDoubleLetter: asdf is {not containsDoubleLetter('.asdf.')}")

# ugknbfddgicrmopn is nice because it has at least three vowels(u...i...o...), a double letter(...dd...), and none of the disallowed substrings.
print(f"ugknbfddgicrmopn: { main('ugknbfddgicrmopn')}")
# aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
print(f"aaa: { main('aaa')}")
# jchzalrnumimnmhp is naughty because it has no double letter.
print(f"jchzalrnumimnmhp { not main('jchzalrnumimnmhp')}")
# haegwjzuvuyypxyu is naughty because it contains the string xy.
print(f"haegwjzuvuyypxyu { not main('haegwjzuvuyypxyu')}")
# dvszwmarrgswjxmb is naughty because it contains only one vowel.
print(f"dvszwmarrgswjxmb { not main('dvszwmarrgswjxmb')}")
print()

# actuals
print("Problem")
with open("./inputs/5.txt", "r") as file:
    lines = file.readlines()

print(f"actual: { sum(main(l) for l in lines)}")
