#!/usr/bin/env python3

def num_set(data):
    s = set()
    for item in data.strip().split(' '):
        if len(item) == 0:
            continue
        s.add(int(item))
    return s

total = 0

with open('day04.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]
    for line in lines:
        data = line.split(': ')[1]
        left, right = data.split(' | ')
        winners, numbers = num_set(left), num_set(right)

        score = 0
        for number in numbers:
            if number in winners:
                if score == 0:
                    score = 1
                else:
                    score *= 2
        total += score

print(f'Part 1: {total}')

count = 0

with open('day04.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]
    counts = {}
    for i in range(len(lines)):
        counts[i] = 1
    for i in range(len(lines)):
        line = lines[i]
        data = line.split(': ')[1]
        left, right = data.split(' | ')
        winners, numbers = num_set(left), num_set(right)
        wins = 0
        for number in numbers:
            if number in winners:
                wins += 1
        if wins > 0:
            this_count = counts[i]
            for j in range(1, wins+1):
                counts[i+j] += this_count
    for i, c in counts.items():
        count += c

print(f'Part 2: {count}')