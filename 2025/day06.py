#!/usr/bin/env python3

import math

lines = []
with open('day06.txt', 'r') as f:
    lines = [l[:-1] if l.endswith('\n') else l for l in f.readlines()]

data = []

for line in lines[:-1]:
    items = [x for x in line.split(' ') if len(x) > 0]
    index = 0
    for item in items:
        if len(data) == index:
            data.append([int(item)])
        else:
            data[index].append(int(item))
        index += 1

ops = [x for x in lines[-1].split(' ') if len(x) > 0]

total = 0

index = 0
for op in ops:
    if op == '*':
        total += math.prod(data[index])
    else:
        total += sum(data[index])
    index += 1

print(total)

width = max([len(line) for line in lines])
height = len(lines) - 1

ops = lines[-1]

total = 0

nums = []
for col in range(width-1, -1, -1):
    digits = []
    for row in range(height):
        line = lines[row]
        if len(line) > col:
            digit = line[col]
            if digit != ' ':
                digits.append(digit)
    if len(digits) == 0:
        continue
    nums.append(int(''.join(digits)))
    if len(ops) > col:
        op = ops[col]
        if op == '*':
            total += math.prod(nums)
            nums = []
        elif op == '+':
            total += sum(nums)
            nums = []

print(total)
