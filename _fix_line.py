with open(r'trainers\efficientnet.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'prefetch_factor' in line and '\\\"' in line:
        print(f"Line {i+1} before: {repr(line)}")
        lines[i] = '            **({\"prefetch_factor\": 2} if num_workers > 0 else {}),\n'
        print(f"Line {i+1} after:  {repr(lines[i])}")

with open(r'trainers\efficientnet.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Done")
