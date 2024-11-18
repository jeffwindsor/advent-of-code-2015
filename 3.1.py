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


def main(moves):
    moves = moves.rstrip('\n')

    current = (0, 0)
    visited = {current}
    for move in moves:
        current = location(current, move)
        visited.add(current)

    return len(visited)


print("Perfectly Spherical Houses in a Vacuum 1")
print()

print("Tests")
print(f"No Moves: { main('') == 1 }")
print(f"One Move: { main('>') == 2 }")
print(f"Return to Origin: { main('^>v<') == 4 }")
print(f"Revisit: { main('^v^v^v^v^v') == 2 }")
print()

# actuals
print("Problem")
moves = Path("./inputs/3.txt").read_text()
print(f"actual: { main(moves)}")
