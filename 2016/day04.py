#!/usr/bin/env python

import md5

data = """ckczppom"""

index = 1

while True:
	s = data + str(index)
	m = md5.md5(s).hexdigest()
	if m.startswith('00000'):
		break
	else:
		index += 1

print index

index = 1

while True:
	s = data + str(index)
	m = md5.md5(s).hexdigest()
	if m.startswith('000000'):
		break
	else:
		index += 1

print index