#!/usr/bin/env python3

# part 1
total = 0

with open('day01.txt', 'r') as f:
    for line in f.readlines():
        first_digit = 0
        last_digit = 0
        for char in line:
            if char.isdigit():
                first_digit = int(char)
                break
        for char in reversed(line):
            if char.isdigit():
                last_digit = int(char)
                break

        total += first_digit * 10 + last_digit

print(f'Part 1: {total}')

# part 2
total = 0

digit_map = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

def get_digit(line, index):
    char = line[index]
    if char.isdigit():
        return int(char)
    sub = line[index:]
    for key, value in digit_map.items():
        if len(sub) >= len(key) and sub[:len(key)] == key:
            return value
    return None

def find_first_digit(line):
    for index in range(len(line)):
        digit = get_digit(line, index)
        if digit is not None:
            return digit

def find_last_digit(lline):
    for index in range(len(line), 0, -1):
        digit = get_digit(line, index-1)
        if digit is not None:
            return digit

with open('day01.txt', 'r') as f:
    for line in f.readlines():
        first_digit = find_first_digit(line)
        last_digit = find_last_digit(line)
        total += first_digit * 10 + last_digit

print(f'Part 2: {total}')
