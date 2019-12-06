#!/usr/bin/env python

range_str = '136760-595730'
range_lower, range_upper = int(range_str.split('-')[0]), int(range_str.split('-')[1])

def is_valid_pwd(pwd, enforce_range=True):
    if enforce_range and pwd < range_lower:
        return False
    if enforce_range and pwd > range_upper:
        return False
    pwd_s = str(pwd).zfill(6)
    char_match = False
    for i in range(5):
        if pwd_s[i] == pwd_s[i+1]:
            char_match = True
        if pwd_s[i] > pwd_s[i+1]:
            return False
    return char_match

count = 0
valid_pwds = []

print(is_valid_pwd(111111, enforce_range=False))
print(is_valid_pwd(223450, enforce_range=False))
print(is_valid_pwd(123789, enforce_range=False))

for pwd in range(1000000):
    if is_valid_pwd(pwd):
        count += 1
        valid_pwds.append(pwd)

print(count, valid_pwds)