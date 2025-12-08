#!/usr/bin/env python3

import itertools
import math

lines = []
with open('day08.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

coords = []
for line in lines:
    coords.append(tuple(int(x) for x in line.split(',')))

circuits = [{x} for x in coords]
limit = 1000

def distance(one, two):
    def dist_sqrd(idx):
        return (two[idx] - one[idx]) ** 2
    return math.sqrt(dist_sqrd(0) + dist_sqrd(1) + dist_sqrd(2))

distances = []

for a, b in itertools.combinations(coords, 2):
    d = distance(a, b)
    distances.append((d, a, b))

distances.sort(key=lambda x: x[0])

for i in range(limit):
    a = distances[i][1]
    b = distances[i][2]
    a_idx, b_idx = -1, -1
    for circuit_idx in range(len(circuits)):
        if a in circuits[circuit_idx]:
            a_idx = circuit_idx
        if b in circuits[circuit_idx]:
            b_idx = circuit_idx
        if a_idx >= 0 and b_idx >= 0:
            break
    if a_idx != b_idx:
        circuits[a_idx].update(circuits[b_idx])
        del circuits[b_idx]

circuit_lens = []
for circuit in circuits:
    circuit_lens.append((len(circuit), circuit))

circuit_lens.sort(key=lambda x: x[0], reverse=True)

total = 1
for i in range(3):
    total *= circuit_lens[i][0]

print(total)

for i in range(limit, len(distances)):
    a = distances[i][1]
    b = distances[i][2]
    a_idx, b_idx = -1, -1
    for circuit_idx in range(len(circuits)):
        if a in circuits[circuit_idx]:
            a_idx = circuit_idx
        if b in circuits[circuit_idx]:
            b_idx = circuit_idx
        if a_idx >= 0 and b_idx >= 0:
            break
    if a_idx != b_idx:
        circuits[a_idx].update(circuits[b_idx])
        del circuits[b_idx]

    if len(circuits) == 1:
        print(a[0] * b[0])
        break

