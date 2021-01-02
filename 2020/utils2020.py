#!/usr/bin/env python

import os, sys

def get_data_filepath(test_data=False):
	# gets the path of this utils2020.py file
	script_filepath = os.path.abspath(__file__)

	# gets the actual script name passed to the python interpreter, like 'day03.py'
	script_filename = os.path.split(sys.argv[0])[-1]
	test_part = '.test' if test_data else ''
	data_filename = os.path.splitext(script_filename)[0] + test_part + '.data'

	data_filepath = os.path.join(os.path.dirname(script_filepath), data_filename)
	return data_filepath

def get_data(test_data=False):
	data = []
	data_filepath = get_data_filepath(test_data=test_data)
	with open(data_filepath, 'r') as f:
		data = f.readlines()
		data = [line.strip() for line in data]
	return data

def get_test_data():
	return get_data(test_data=True)
	