#!/usr/bin/env python3

import math

lines = []
with open('day08.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]


class CommandGenerator(object):
    def __init__(self, command_list):
        self.index = 0
        self.command_list = command_list

    def next(self):
        command = self.command_list[self.index]
        self.index += 1
        if self.index >= len(self.command_list):
            self.index = 0
        return command


class Node(object):
    def __init__(self, left, right):
        self.left = left
        self.right = right


node_map = {}
start_keys = set()
for line in lines[2:]:
    key, values = line.split(' = ')
    left, right = values[1:-1].split(', ')
    node_map[key] = Node(left, right)
    if key.endswith('A'):
        start_keys.add(key)

command_generator = CommandGenerator(lines[0])

current_key = 'AAA'
step_count = 0
while current_key != 'ZZZ':
    node = node_map[current_key]
    command = command_generator.next()
    current_key = node.left if command == 'L' else node.right
    step_count += 1

print(f'Part 1: {step_count}')

command_generator = CommandGenerator(lines[0])

keys = list(start_keys)
cycle_lengths = [0 for key in start_keys]
step_count = 0
while any([l == 0 for l in cycle_lengths]):
    command = command_generator.next()
    new_keys = []
    for key_index in range(len(keys)):
        current_key = keys[key_index]
        if current_key.endswith('Z'):
            print(f'Found cycle length {step_count} for key index {key_index}')
            cycle_lengths[key_index] = step_count
        node = node_map[current_key]
        new_key = node.left if command == 'L' else node.right
        new_keys.append(new_key)
    keys = new_keys
    step_count += 1

total = math.lcm(*cycle_lengths)

print(f'Part 2: {total}')
