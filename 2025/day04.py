#!/usr/bin/env python3

lines = []
with open('day04.txt', 'r') as f:
    lines = [list(l.strip()) for l in f.readlines()]

width, height = len(lines[0]), len(lines)
c1, c2 = 0, 0

for y in range(height):
    print(''.join(lines[y]))
print()

first_pass = True

while True:
    remove = []

    for y in range(height):
        for x in range(width):
            if lines[y][x] != '@':
                continue
            adj = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    xi, yj = x + i, y + j
                    if width > xi >= 0 and height > yj >= 0:
                        if lines[yj][xi] == '@':
                            adj += 1
            if adj < 4:
                if first_pass:
                    c1 += 1
                c2 += 1
                remove.append((y, x))

    if len(remove) == 0:
        break

    first_pass = False

    for y in range(height):
        for x in range(width):
            if lines[y][x] == 'x':
                lines[y][x] = '.'

    for y, x in remove:
        lines[y][x] = 'x'

    for y in range(height):
        print(''.join(lines[y]))
    print()


print(c1)
print(c2)
