#!/usr/bin/env python3

lines = []
with open('day05.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

ranges = []
available = []

found_empty = False
for line in lines:
    if len(line) == 0:
        found_empty = True
        continue
    if found_empty:
        available.append(int(line))
    else:
        ranges.append([int(x) for x in line.split('-')])

ranges.sort(key=lambda x: x[0])

i, j = 0, len(ranges) - 1
while i < j:
    if ranges[i][1] >= ranges[i+1][0]:
        ranges[i:i+2] = [[ranges[i][0], max(ranges[i][1], ranges[i+1][1])]]
        j -= 1
    else:
        i += 1

fresh = 0

for a in available:
    for r in ranges:
        if r[0] <= a <= r[1]:
            fresh += 1
            break

print(fresh)

fresh = 0

for r in ranges:
    fresh += r[1] - r[0] + 1

print(fresh)
