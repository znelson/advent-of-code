#!/usr/bin/env python3

# part 1
total = 0

# part 2
power = 0

with open('day02.txt', 'r') as f:
	for line in f.readlines():
		(game, line) = line.split(': ')
		line = line.strip()
		game = int(game.split(' ')[1])
		limits = {}
		for handful in line.split('; '):
			dice = handful.split(', ')
			for die in dice:
				(count, color) = die.split(' ')
				count = int(count)
				if color not in limits or count > limits[color]:
					limits[color] = count
		red = limits.get('red', 0)
		green = limits.get('green', 0)
		blue = limits.get('blue', 0)
		if red <= 12 and green <= 13 and blue <= 14:
			total += game
		power += red * green * blue

print(f'Part 1: {total}')
print(f'Part 2: {power}')

