from pathlib import Path


def location(origin, move):
    if move == ">":
        return (origin[0], origin[1]+1)
    elif move == "<":
        return (origin[0], origin[1]-1)
    elif move == "^":
        return (origin[0]+1, origin[1])
    elif move == "v":
        return (origin[0]-1, origin[1])
    else:
        print(f"Bad Data {origin} move {move}")
        return origin


def locations(moves):
    current = (0, 0)
    visited = {current}
    for move in moves:
        current = location(current, move)
        visited.add(current)
    return visited


def main(moves):
    moves = moves.rstrip('\n')
    santa = locations([move for i, move in enumerate(moves) if i % 2 == 0])
    rsanta = locations([move for i, move in enumerate(moves) if i % 2 != 0])
    # print(santa)
    # print(rsanta)
    return len(santa.union(rsanta))


print("Perfectly Spherical Houses in a Vacuum 2")
print()

print("Tests")
print(f"No Moves: { main('') == 1 }")
print(f"One Move: { main('^v') == 3 }")
print(f"Return to Origin: { main('^>v<') == 3 }")
print(f"Revisit: { main('^v^v^v^v^v') == 11 }")
print()

# actuals
print("Problem")
moves = Path("./inputs/3.txt").read_text()
print(f"actual: { main(moves)}")
