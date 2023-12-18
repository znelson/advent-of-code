#!/usr/bin/env python3

lines = []
with open('day05.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]


class RangeMapping(object):
    def __init__(self, line):
        numbers = line.split(' ')
        self.d_start = int(numbers[0])
        self.s_start = int(numbers[1])
        self.length = int(numbers[2])

    @property
    def d_end(self):
        return self.d_start + self.length - 1

    @property
    def s_end(self):
        return self.s_start + self.length - 1

    def contains(self, n):
        return self.s_start <= n <= self.s_end

    def convert(self, n):
        offset = n - self.s_start
        return self.d_start + offset

    def __str__(self):
        return f'<RangeMapping len={self.length}, s={self.s_start}->{self.s_end}, d={self.d_start}->{self.d_end}>'

    def __repr__(self):
        return str(self)


class GardenMap(object):

    def __init__(self):
        self.mappings = []

    def add_mapping(self, line):
        self.mappings.append(RangeMapping(line))

    def __str__(self):
        map_str = ', '.join([str(m) for m in self.mappings])
        return f'<GardenMap: {map_str}>'

    def __repr__(self):
        return str(self)

    def convert(self, n):
        for m in self.mappings:
            if m.contains(n):
                return m.convert(n)
        return n


maps = {}

map_name = ''
map_helper = None

for line in lines:
    if line.endswith(' map:'):
        map_name = line.split(' ')[0]
        map_helper = GardenMap()
    elif len(line) == 0 and len(map_name) > 0:
        maps[map_name] = map_helper
    elif map_helper:
        map_helper.add_mapping(line)
maps[map_name] = map_helper

maps_in_order = [
    maps['seed-to-soil'],
    maps['soil-to-fertilizer'],
    maps['fertilizer-to-water'],
    maps['water-to-light'],
    maps['light-to-temperature'],
    maps['temperature-to-humidity'],
    maps['humidity-to-location'],
]


def seed_to_location(seed):
    value = seed
    for m in maps_in_order:
        value = m.convert(value)
    return value


seeds = [int(seed) for seed in lines[0].split(': ')[1].split(' ')]
print(f'Seeds: {seeds}')

min_location = None

for seed in seeds:
    location = seed_to_location(seed)
    if min_location is None or location < min_location:
        min_location = location

print(f'Part 1: {min_location}')


class EquivalenceClass(object):
    def __init__(self, start, count):
        self.start = start
        self.count = count

    @property
    def end(self):
        return self.start + self.count - 1

    def __str__(self):
        return f'<EquivalenceClass: {self.start},{self.count}->{self.end}>'

    def __repr__(self):
        return str(self)

    def intersect(self, eqcl):
        # eqcl is a superset of this range
        if eqcl.start <= self.start and eqcl.end >= self.end:
            return [self]

        # eqcl is above this range
        if eqcl.start > self.end and eqcl.end > self.end:
            return [self]

        # eqcl is below this range
        if eqcl.start < self.start and eqcl.end < self.start:
            return [self]

        # eqcl overlaps left
        elif eqcl.start <= self.start < eqcl.end <= self.end:
            c1 = eqcl.end - self.start + 1
            c2 = self.end - eqcl.end
            s2 = eqcl.end + 1
            return [
                EquivalenceClass(self.start, c1),
                EquivalenceClass(s2, c2),
            ]

        # eqcl overlaps right
        elif eqcl.end >= self.end > eqcl.start >= self.start:
            c1 = eqcl.start - self.start
            c2 = self.end - eqcl.start + 1
            return [
                EquivalenceClass(self.start, c1),
                EquivalenceClass(eqcl.start, c2),
            ]

        # eqcl is subset of this range
        elif eqcl.start > self.start and eqcl.end < self.end:
            c1 = eqcl.start - self.start
            c2 = eqcl.end - eqcl.start + 1
            c3 = self.end - eqcl.end
            s3 = eqcl.end + 1
            return [
                EquivalenceClass(self.start, c1),
                EquivalenceClass(eqcl.start, c2),
                EquivalenceClass(s3, c3),
            ]


min_location = None

for i in range(int(len(seeds) / 2)):
    index = i * 2
    start, count = seeds[index], seeds[index+1]
    eqcl = EquivalenceClass(start, count)

    eqcls = [eqcl]

    for mp in maps_in_order:
        for m in mp.mappings:
            map_eqcl = EquivalenceClass(m.s_start, m.length)
            new_eqcls = []
            for old_eqcl in eqcls:
                new_eqcls.extend(old_eqcl.intersect(map_eqcl))
            eqcls = new_eqcls

        new_eqcls = []
        for old_eqcl in eqcls:
            new_eqcls.append(EquivalenceClass(mp.convert(old_eqcl.start), old_eqcl.count))
        eqcls = new_eqcls

    for eqcl in eqcls:
        if min_location is None or eqcl.start < min_location:
            min_location = eqcl.start


print(f'Part 2: {min_location}')
