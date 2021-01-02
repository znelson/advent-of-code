#!/usr/bin/env python

import utils2020

data = utils2020.get_data()

parsed_data = []
parsed_datum = {}

for datum in data:
	if len(datum) == 0:
		parsed_data.append(parsed_datum)
		parsed_datum = {}
	else:
		fields = datum.split(' ')
		for field in fields:
			key, value = field.split(':')
			parsed_datum[key] = value

if len(parsed_datum) > 0:
	parsed_data.append(parsed_datum)
	parsed_datum = {}

valid_passports = 0

for datum in parsed_data:
	if 'byr' in datum and 'iyr' in datum and 'eyr' in datum and 'hgt' in datum and 'hcl' in datum and 'ecl' in datum and 'pid' in datum:
		valid_passports += 1

print(valid_passports)

valid_passports = 0

for datum in parsed_data:
	
	try:
		birth_year = int(datum['byr'])
		if birth_year < 1920 or birth_year > 2002:
			continue
	except:
		continue

	try:
		issue_year = int(datum['iyr'])
		if issue_year < 2010 or issue_year > 2020:
			continue
	except:
		continue

	try:
		expire_year = int(datum['eyr'])
		if expire_year < 2020 or expire_year > 2030:
			continue
	except:
		continue

	try:
		height = int(datum['hgt'][:-2])
		units = datum['hgt'][-2:]
		if units != 'cm' and units != 'in':
			continue
		if units == 'cm' and (height < 150 or height > 193):
			continue
		if units == 'in' and (height < 59 or height > 76):
			continue
	except:
		continue

	try:
		hair_color = datum['hcl']
		if len(hair_color) != 7 or hair_color[0] != '#':
			continue
		for i in range(1,7):
			c = hair_color[i]
			if not ('0' <= c <= '9' or 'a' <= c <= 'f'):
				continue
	except:
		continue
	
	try:
		eye_color = datum['ecl']
		if eye_color != 'amb' and eye_color != 'blu' and eye_color != 'brn' and eye_color != 'gry' and eye_color != 'grn' and eye_color != 'hzl' and eye_color != 'oth':
			continue
	except:
		continue

	try:
		passport_id = datum['pid']
		if len(passport_id) != 9:
			continue
		passport_id = int(passport_id)
	except:
		continue

	valid_passports += 1

print(valid_passports)

