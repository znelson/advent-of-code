#!/usr/bin/env python3

lines = []
with open('day09.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

def same(l):
    x = l[0]
    for i in range(1, len(l)):
        if l[i] != x:
            return False
    return True


future = 0
past = 0

for line in lines:
    numbers = [int(n) for n in line.split(' ')]

    gaps = [numbers]
    while not same(numbers):
        gap = []
        for i in range(1, len(numbers)):
            diff = numbers[i] - numbers[i-1]
            gap.append(diff)
        gaps.append(gap)
        numbers = gap

    for i in range(len(gaps)-1, 0, -1):
        diff_last = gaps[i][-1]
        last = gaps[i-1][-1]
        diff_first = gaps[i][0]
        first = gaps[i-1][0]
        gaps[i-1].append(last+diff_last)
        gaps[i-1].insert(0, first-diff_first)

    future += gaps[0][-1]
    past += gaps[0][0]

print(f'Part 1: {future}')
print(f'Part 2: {past}')
