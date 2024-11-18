from pathlib import Path
from itertools import groupby

input = Path("./inputs/1.txt").read_text()
groups = groupby(sorted(input))
with_counts = [(k, len(list(g))) for k, g in groups]

print(with_counts)
