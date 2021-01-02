#!/usr/bin/env python

import utils2020

data = utils2020.get_data()

total_answers = 0
group_answers = set()
for line in data:
	if len(line) == 0:
		total_answers += len(group_answers)
		group_answers = set()
	else:
		list(map(lambda c: group_answers.add(c), line))
total_answers += len(group_answers)
print(total_answers)

def default_set():
	ds = set()
	list(map(lambda c: ds.add(chr(c)), range(ord('a'), ord('z'))))
	return ds

total_answers = 0
group_answers = default_set()
for line in data:
	if len(line) == 0:
		total_answers += len(group_answers)
		print(len(group_answers), total_answers, group_answers)
		group_answers = default_set()
	elif len(group_answers) > 0:
		line_answers = set()
		list(map(lambda c: line_answers.add(c), line))
		group_answers.intersection_update(line_answers)
total_answers += len(group_answers)
print(len(group_answers), total_answers, group_answers)
print(total_answers)