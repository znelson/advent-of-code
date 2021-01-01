#!/usr/bin/env python

data = """cqjxjnds"""

# ord('a') = 97
# ord('z') = 122

def increment(password):
	i = len(password) - 1

	while i > 0:
		o = ord(password[i]) + 1
		if o > 122:
			password = password[0:i] + 'a' + password[i+1:]
			i -= 1
		else:
			password = password[0:i] + chr(o) + password[i+1:]
			break

	return password

def test_rule_1(password):
	i = 0
	for i in range(len(password) - 2):
		part = password[i:i+3]
		if ord(part[0]) + 1 == ord(part[1]):
			if ord(part[1]) + 1 == ord(part[2]):
				return True
	return False

def test_rule_2(password):
	if 'i' in password:
		return False
	elif 'o' in password:
		return False
	elif 'l' in password:
		return False
	return True

def test_rule_3(password):
	doubles = set()
	i = 0
	for i in range(len(password) - 1):
		part = password[i:i+2]
		if part[0] == part[1]:
			doubles.add(part)
	return len(doubles) > 1

def test(password):
	return test_rule_1(password) and test_rule_2(password) and test_rule_3(password)


password = data
while not test(password):
	password = increment(password)

print(password)

password = increment(password)
while not test(password):
	password = increment(password)

print(password)