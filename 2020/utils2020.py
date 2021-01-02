#!/usr/bin/env python

import os, sys

def get_data_filepath():
	# gets the path of this utils2020.py file
	script_filepath = os.path.abspath(__file__)

	# gets the actual script name passed to the python interpreter, like 'day03.py'
	script_filename = os.path.split(sys.argv[0])[-1]
	data_filename = os.path.splitext(script_filename)[0] + '.data'

	data_filepath = os.path.join(os.path.dirname(script_filepath), data_filename)
	return data_filepath

def get_data():
	data = []
	data_filepath = get_data_filepath()
	with open(data_filepath, 'r') as f:
		data = f.readlines()
		data = [line.strip() for line in data]
	return data
	