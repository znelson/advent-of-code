#!/usr/bin/env python

import utils2020

data = utils2020.get_data()
data = [int(x) for x in data]

result = 0

for i in range(len(data)):
	for j in range(i+1, len(data)):
		x = data[i]
		y = data[j]
		if (x + y) == 2020:
			result = x * y
			break
	if result > 0:
		break

print(result)

result = 0

for i in range(len(data)):
	for j in range(i+1, len(data)):
		for k in range(j+1, len(data)):
			x = data[i]
			y = data[j]
			z = data[k]
			if (x + y + z) == 2020:
				result = x * y * z
				break
		if result > 0:
			break
	if result > 0:
		break

print(result)
