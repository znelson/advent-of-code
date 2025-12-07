#!/usr/bin/env python3

lines = []
with open('day07.txt', 'r') as f:
    lines = [list(l.strip()) for l in f.readlines()]

beams = {lines[0].index('S'): 1}
splits = 0

for row in range(1, len(lines)):
    line = lines[row]
    for beam, tl_count in beams.copy().items():
        if line[beam] == '^':
            del beams[beam]
            for new_beam in {beam-1, beam+1}:
                if new_beam in beams:
                    beams[new_beam] += tl_count
                else:
                    beams[new_beam] = tl_count
            splits += 1
    for beam in beams:
        line[beam] = '|'

    for line in lines:
        print(''.join(line))
    print()

print(splits)

timelines = 0
for _, tl_count in beams.items():
    timelines += tl_count

print(timelines)
