"""Fix bare prefetch_factor=2 in all trainer files."""

files = [
    r"trainers\fastervit.py",
    r"trainers\efficientformer_v2.py",
    r"trainers\efficientnet.py",
]

OLD = "            prefetch_factor=2,\n"
NEW = '            **({"prefetch_factor": 2} if num_workers > 0 else {}),\n'

for path in files:
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    changed = 0
    for i, line in enumerate(lines):
        if line == OLD:
            lines[i] = NEW
            changed += 1

    with open(path, "w", encoding="utf-8") as f:
        f.writelines(lines)

    print(f"{path}: fixed {changed} line(s)")
