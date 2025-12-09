#!/usr/bin/env python3

import itertools

def min_max_x_y(one, two):
    x0, x1 = min(one[0], two[0]), max(one[0], two[0])
    y0, y1 = min(one[1], two[1]), max(one[1], two[1])
    return x0, x1, y0, y1

# Check if a point lies within the polygon
def contains_point(point, vertices):
    x, y = point
    inside = False

    for i in range(len(vertices)-1):
        # Count vertical edges to test if point is inside or outside
        vx, _, y0, y1 = min_max_x_y(vertices[i], vertices[i+1])
        if y0 != y1 and y0 <= y < y1 and x >= vx:
            inside = not inside

    return inside

# Check if a rectangle's edges intersect edges of a polygon
# one and two are opposite corners of a rectangle
def edges_intersect(one, two, vertices):
    x0, x1, y0, y1 = min_max_x_y(one, two)

    for i in range(len(vertices)-1):
        v_x0, v_x1, v_y0, v_y1 = min_max_x_y(vertices[i], vertices[i+1])

        if v_x0 == v_x1:
            # Vertices make a vertical edge, check the two horizontal rect edges
            if x0 < v_x0 < x1:
                if v_y0 < y0 < v_y1 or v_y0 < y1 < v_y1:
                    return True
        else:
            # Vertices make a horizontal edge, check the two vertical rect edges
            if y0 < v_y0 < y1:
                if v_x0 < x0 < v_x1 or v_x0 < x1 < v_x1:
                    return True

    return False

# Check if a rectangle's is fully contained within a polygon
# one and two are opposite corners of a rectangle
def contains_rect(one, two, vertices):
    # Corners one and two are already in the vertices list so no need to check them
    for p in [(one[0], two[1]), (two[0], one[1])]:
        if not contains_point(p, vertices):
            return False
    return not edges_intersect(one, two, vertices)

if __name__ == '__main__':
    lines = []
    with open('day09.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]

    coords = []
    for line in lines:
        coords.append(tuple(int(x) for x in line.split(',')))

    areas = []

    for a, b in itertools.combinations(coords, 2):
        width, height = abs(a[0] - b[0]) + 1, abs(a[1] - b[1]) + 1
        areas.append((width * height, a, b))

    areas.sort(key=lambda x: x[0], reverse=True)

    print(areas[0][0])

    # Close the polygon
    coords.append(coords[0])

    for area, a, b in areas:
        if contains_rect(a, b, coords):
            print(area)
            break
