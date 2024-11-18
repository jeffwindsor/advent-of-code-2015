def perimeter(a, b):
    return 2 * (a + b)


def ribbon_length(dimensions):
    # split dimensions into l,w,h
    ds = [int(d) for d in dimensions.split('x')]
    least_perimeter = min([perimeter(ds[0], ds[1]),
                           perimeter(ds[0], ds[2]),
                           perimeter(ds[1], ds[2])])
    cubic = ds[0] * ds[1] * ds[2]
    return least_perimeter + cubic


print(ribbon_length("2x3x4") == 34)
print(ribbon_length("1x1x10") == 14)

with open("./inputs/2.txt", "r") as file:
    lines = file.readlines()

print(sum([ribbon_length(line) for line in lines]))
