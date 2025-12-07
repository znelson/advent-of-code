#!/usr/bin/env python3

lines = []
with open('day02.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

t1 = 0
t2 = 0

for line in lines:
    ranges = line.split(',')
    for r in ranges:
        a, b = [int(x) for x in r.split('-')]
        for i in range(a, b+1):
            s = str(i)
            l = len(s)
            if l % 2 == 0:
                x, y = s[:l//2], s[l//2:]
                if x == y:
                    t1 += i
            for j in range(1, l//2+1):
                if l % j == 0:
                    p = []
                    for k in range(l // j):
                        p.append(s[k*j:(k+1)*j])
                    m = True
                    for q in p[1:]:
                        if p[0] != q:
                            m = False
                            break
                    if m:
                        t2 += i
                        break




print(t1)
print(t2)
