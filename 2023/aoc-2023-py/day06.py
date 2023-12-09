#!/usr/bin/env python3

lines = []
with open('day06.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

times = [int(t) for t in lines[0].split(':')[1].split(' ') if len(t) > 0]
distances = [int(d) for d in lines[1].split(':')[1].split(' ') if len(d) > 0]
result = 1

def count_wins(time, distance):
    win_count = 0
    for ms in range(time + 1):
        speed, travel_time = ms, time - ms
        d = speed * travel_time
        if d > distance:
            win_count += 1
    return win_count

for index in range(len(times)):
    result *= count_wins(times[index], distances[index])

print(f'Part 1: {result}')

time = int(lines[0].split(':')[1].replace(' ', ''))
distance = int(lines[1].split(':')[1].replace(' ', ''))
result = count_wins(time, distance)

print(f'Part 2: {result}')

