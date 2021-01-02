#!/usr/bin/env python

import time, utils2020

data = utils2020.get_data()

time0 = time.perf_counter()

parsed_data = []

for datum in data:
	datum, password = datum.split(': ')
	datum, letter = datum.split(' ')
	num_one, num_two = datum.split('-')
	num_one, num_two = int(num_one), int(num_two)
	parsed_data.append((num_one, num_two, letter, password))

time1 = time.perf_counter()
print('Parsed in {0} seconds'.format(time1 - time0))

valid_passwords = 0

for min_count, max_count, letter, password in parsed_data:
	match_count = 0
	for match in filter(lambda x: x == letter, password):
		match_count += 1
		if match_count > max_count:
			break
	if min_count <= match_count <= max_count:
		valid_passwords += 1

time2 = time.perf_counter()
print(valid_passwords, 'Processed in {0} seconds'.format(time2 - time1))

valid_passwords = 0

for index_one, index_two, letter, password in parsed_data:
	if len(password) < index_one or len(password) < index_two:
		continue
	index_one -= 1
	index_two -= 1
	if (password[index_one] == letter) ^ (password[index_two] == letter):
		valid_passwords += 1

time3 = time.perf_counter()
print(valid_passwords, 'Processed in {0} seconds'.format(time3 - time2))

total_ms = (time3 - time0) * 1000
print(f'Total time {total_ms} milliseconds')