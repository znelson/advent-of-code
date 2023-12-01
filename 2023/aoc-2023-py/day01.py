#!/usr/bin/env python3

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

print(total)
