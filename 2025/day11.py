#!/usr/bin/env python3

from functools import cache

lines = []
with open('day11.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

connections = {}
for line in lines:
    name, outs = line.split(': ')
    connections[name] = outs.split(' ')

@cache
def count_paths(key, end):
    if key == end:
        return 1
    return sum(count_paths(value, end) for value in connections[key])

@cache
def count_dac_fft_paths(key, end, found_dac=False, found_fft=False):
    if key == end:
        return 1 if found_dac and found_fft else 0
    if key == 'dac':
        found_dac = True
    elif key == 'fft':
        found_fft = True
    return sum(count_dac_fft_paths(value, end, found_dac, found_fft) for value in connections[key])

print(count_paths('you', 'out'))
print(count_dac_fft_paths('svr', 'out'))
