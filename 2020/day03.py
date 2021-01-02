#!/usr/bin/env python

import utils2020

data = utils2020.get_data()

slopes = [1, 3, 5, 7, 0.5]
trees = []

for slope in slopes:
	x = 0
	t = 0
	for line in data:
		if int(x) == float(x):
			x = x % len(line)
			if line[int(x)] == '#':
				t += 1
		x += slope
	trees.append(t)

print(trees[1])

total = 1
for t in trees:
	total *= t

print(total)