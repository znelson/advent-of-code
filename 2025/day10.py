#!/usr/bin/env python3

import itertools
import pulp

def find_min_buttons(target, buttons):
    if target == 0:
        return 0
    masks = [int(''.join([str(x) for x in b]), 2) for b in buttons]
    for count in range(1, len(masks)+1):
        for combo in itertools.combinations(masks, count):
            result = 0
            for button in combo:
                result ^= button
            if result == target:
                return count
    raise RuntimeError('No button combination found')

# Brute force is too slow
def find_min_coefficients(target, buttons):
    start = (0,) * len(target)
    if all(x == y for x, y in zip(start, target)):
        return 0
    search = [(start, 0)]
    visited = {start}
    while len(search):
        value, count = search.pop(0)
        for button in buttons:
            new_value = tuple(x + y for x, y in zip(value, button))
            if any(x > y for x, y in zip(new_value, target)):
                continue
            if all(x == y for x, y in zip(new_value, target)):
                return count + 1
            if new_value not in visited:
                visited.add(new_value)
                search.append((new_value, count + 1))
    return 0

def find_min_coefficients_pulp(target, buttons):
    problem = pulp.LpProblem(sense=pulp.LpMinimize)
    variables = []
    for i in range(len(buttons)):
        variables.append(pulp.LpVariable(f'coefficient_{i}', lowBound=0, cat=pulp.LpInteger))
    problem += pulp.lpSum(variables), 'coefficient_sum'
    for i in range(len(target)):
        problem += pulp.lpSum(variables[j] * buttons[j][i] for j in range(len(buttons))) == target[i], f'dimension_{i}'
    status = problem.solve(pulp.PULP_CBC_CMD(msg=False))
    if pulp.LpStatus[status] != 'Optimal':
        raise RuntimeError('No button combination found')
    return sum(int(pulp.value(variables[i])) for i in range(len(buttons)))

if __name__ == '__main__':
    lines = []
    with open('day10.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]

    lights = []
    buttons = []
    joltages = []

    for line in lines:
        tokens = line.split(' ')

        l = tokens[0][1:-1].replace('.', '0').replace('#', '1')
        lights.append(int(l, 2))

        buttons.append([])
        for token in tokens[1:-1]:
            indices = [int(x) for x in token[1:-1].split(',')]
            b = [0] * len(l)
            for index in indices:
                b[index] = 1
            buttons[-1].append(b)

        j = tokens[-1][1:-1]
        joltages.append([int(x) for x in j.split(',')])

    one, two = 0, 0

    for i in range(len(lights)):
        one += find_min_buttons(lights[i], buttons[i])
        two += find_min_coefficients_pulp(joltages[i], buttons[i])

    print(one)
    print(two)
