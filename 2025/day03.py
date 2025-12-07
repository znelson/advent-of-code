#!/usr/bin/env python3

import re

lines = []
with open('day03.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

total = 0

for line in lines:
    joltage = 99
    while joltage > 0:
        a, b = f'{joltage:02d}'
        r = re.compile(f'.*{a}.*{b}.*')
        if r.match(line):
            total += joltage
            break
        joltage -= 1

print(total)

total = 0
size = 12

for line in lines:
    num = []
    pos = 0
    while len(num) < size:
        reserved = size - len(num) - 1
        search = line[pos:-reserved] if reserved else line[pos:]
        digit = max(search)
        num.append(digit)
        pos = search.find(digit) + pos + 1

    total += int(''.join(num))

print(total)
