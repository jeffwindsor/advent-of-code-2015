
def paper_needed(dimensions):
    # split dimensions into l,w,h
    ds = [int(d) for d in dimensions.split('x')]
    # calculate areas
    areas = [ds[0] * ds[1], ds[0] * ds[2], ds[1] * ds[2]]
    smallest = min(areas)
    # add extra paper equal to the smallest diminsion

    return (2 * sum(areas)) + smallest


# A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
print(paper_needed("2x3x4") == 58)
# A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.
print(paper_needed("1x1x10") == 43)

with open("./inputs/2.txt", "r") as file:
    lines = file.readlines()

print(sum([paper_needed(line) for line in lines]))
