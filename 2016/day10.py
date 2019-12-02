#!/usr/bin/env python

data = """3113322113"""

def rewrite(num):
	last = num[0]
	count = 1
	out = ''
	for c in num[1:]:
		if c == last:
			count += 1
		else:
			out += str(count) + last
			last = c
			count = 1
	if count > 0:
		out += str(count) + last
	return out

s = data
for i in range(40):
	s = rewrite(s)

print len(s)

s = data
for i in range(50):
	s = rewrite(s)

print len(s)