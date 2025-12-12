#!/usr/bin/env python3

lines = []
with open('day12.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

sizes = []
size = 0
for line in lines:
    if ':' in line or 'x' in line:
        continue
    if not line:
        sizes.append(size)
        size = 0
        continue
    size += line.count('#')

valid = 0
for line in lines:
    if 'x' in line:
        one, two = line.split(': ')
        x, y = (int(x) for x in one.split('x'))
        area = x * y
        counts = (int(x) for x in two.split(' '))
        size = sum(c * sizes[i] for i, c in enumerate(counts))
        if size <= area:
            valid += 1

print(valid)
