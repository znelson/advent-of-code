#!/usr/bin/env python

import utils2020

data = utils2020.get_data()

seats = set(range(1024))

largest_seat = 0

for line in data:
	row = 0
	col = 0
	row_modifier = 64
	col_modifier = 4
	for c in line:
		if c == 'B' or c == 'F':
			if c == 'B':
				row += row_modifier
			row_modifier /= 2
		elif c == 'L' or c == 'R':
			if c == 'R':
				col += col_modifier
			col_modifier /= 2
	seat = int(row * 8 + col)
	largest_seat = max(seat, largest_seat)
	seats.remove(seat)

print(largest_seat)

for seat in sorted(list(seats)):
	if (seat-1) not in seats and (seat+1) not in seats:
		print(seat)