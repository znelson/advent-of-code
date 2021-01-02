#!/usr/bin/env python

import utils2020

data = utils2020.get_data()

container_mapping = {}

for line in data:
	words = line.split(' ')
	if words[4] == 'no':
		continue
	
	container_color = words[0] + ' ' + words[1]

	contained = {}

	count_index = 4
	while count_index < len(words):
		contained_count = int(words[count_index])
		contained_color = words[count_index+1] + ' ' + words[count_index+2]
		contained[contained_color] = contained_count
		count_index += 4
	
	container_mapping[container_color] = contained

compatible_containers = set()
colors_to_process = {'shiny gold'}
while len(colors_to_process) > 0:
	color_to_process = colors_to_process.pop()
	for key, value in container_mapping.items():
		if color_to_process in value:
			colors_to_process.add(key)
			compatible_containers.add(key)
print(len(compatible_containers))

total_bags = 0
bags_to_process = container_mapping['shiny gold']
print(bags_to_process)
while len(bags_to_process) > 0:
	bag_color, bag_count = bags_to_process.popitem()
	print(f'Processing {bag_count} {bag_color} bag(s)')
	total_bags += bag_count
	if bag_color in container_mapping:
		bags_to_add = container_mapping[bag_color]
		for key, value in bags_to_add.items():
			if key in bags_to_process:
				bags_to_process[key] += bag_count * value
			else:
				bags_to_process[key] = bag_count * value
print(total_bags)
