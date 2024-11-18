
import hashlib


def main(prefix):
    postfix = 0
    while True:
        key = prefix + str(postfix)
        if hashlib.md5(key.encode()).hexdigest().startswith('000000'):
            return postfix
        postfix += 1


print("The Ideal Stocking Stuffer")
print()

print("Tests")
print(f"abcdef: { main('abcdef') == 609043 }")
print(f"pqrstuv: { main('pqrstuv') == 1048970}")
print()

# actuals
print("Problem")
print(f"actual: { main('bgvyzdsv')}")
