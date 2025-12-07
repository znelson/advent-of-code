#!/usr/bin/env python3

lines = []
with open('day01.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

c1 = 0
c2 = 0
position = 50

for line in lines:
    left = line[0] == 'L'
    num = int(line[1:])
    if left:
        num = -num
    position += num
    c2 += abs(position // 100)
    position %= 100
    if position == 0:
        c1 += 1

print(c1)
print(c2)
