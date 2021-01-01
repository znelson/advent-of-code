#!/usr/bin/env python

import hashlib

data = """ckczppom"""

index = 1

while True:
	s = data + str(index)
	m = hashlib.md5(s.encode('utf-8')).hexdigest()
	if m.startswith('00000'):
		break
	else:
		index += 1

print(index)

index = 1

while True:
	s = data + str(index)
	m = hashlib.md5(s.encode('utf-8')).hexdigest()
	if m.startswith('000000'):
		break
	else:
		index += 1

print(index)