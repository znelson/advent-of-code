#!/usr/bin/env python

import itertools

data = """11
30
47
31
32
36
3
1
5
3
32
36
15
11
46
26
28
1
19
3"""

eggnog = 150

containers = [int(x) for x in data.split('\n')]
# print(containers)

valid_combos = 0

min_containers = len(containers)
min_count = 0

for i in range(1, len(containers) + 1):
	# print('Trying combinations of {0} containers'.format(i))
	for containers_combination in itertools.combinations(containers, i):

		if sum(containers_combination) == eggnog:
			# print(containers_combination)
			valid_combos += 1

			if i < min_containers:
				# print('Setting min containers to {0}'.format(i))
				min_containers = i

			if i == min_containers:
				min_count += 1

print(valid_combos)
print(min_count)