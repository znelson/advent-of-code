#!/usr/bin/env python3

with open('day03.txt', 'r') as f:
	lines = [l.strip() for l in f.readlines()]
	
	parts = {}
	col, row = 0, 0
	for line in lines:
		for char in line:
			if char != '.' and not char.isdigit():
				parts[(col, row)] = char
			col += 1
		row += 1
		col = 0
	
	gears = {}
	col, row = 0, 0
	
	def check_part(number):
		if len(number) > 0:
			positions = []
			for x in range(col-len(number)-1, col+1):
				for y in range(row-1, row+2):
					positions.append((x, y))
			for position in positions:
				if position in parts:
					n = int(number)
					if parts[position] == '*':
						if position not in gears:
							gears[position] = [n]
						else:
							gears[position].append(n)
					return n
		return 0
	
	total = 0
	for line in lines:
		number = ''
		for char in line:
			if char.isdigit():
				number += char
			else:
				total += check_part(number)
				number = ''
			col += 1
		total += check_part(number)
		row += 1
		col = 0
	
	ratios = 0
	for position, numbers in gears.items():
		if len(numbers) == 2:
			ratios += numbers[0] * numbers[1]

print(f'Part 1: {total}')
print(f'Part 2: {ratios}')

