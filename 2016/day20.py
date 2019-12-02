#!/usr/bin/env python

limit = 3600000

def house_count(house_number):
	count = 1
	if house_number > 1:
		loop_limit = int((house_number+1) / 2.) + 1
		for i in xrange(2, loop_limit):
			if house_number % i == 0:
				count += i
		count += house_number
	return count

for i in range(12):
	print i, house_count(i)


# 1  = 1 = 1
# 2  = 3 = 1 + 2
# 3  = 4 = 1 + 3
# 4  = 7 = 1 + 2 + 4
# 5  = 6 = 1 + 5
# 6  = 12 = 1 + 2 + 3 + 6
# 7  = 8 = 1 + 7
# 8  = 15 = 1 + 2 + 4 + 8
# 9  = 13 = 1 + 3 + 9
# 10 = 18 = 1 + 2 + 5 + 10
# 11 = 12 = 1 + 11