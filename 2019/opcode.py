#!/usr/bin/env python

import enum

"""
ABCDE
 1002

DE - two-digit opcode,      02 == opcode 2
 C - mode of 1st parameter,  0 == position mode
 B - mode of 2nd parameter,  1 == immediate mode
 A - mode of 3rd parameter,  0 == position mode, omitted due to being a leading zero
"""

class OpcodeMode(enum.Enum):
	POSITION = 0
	IMMEDIATE = 1

class Opcode:
	def __init__(self, tape, index):
		cmd = str(tape[index]).zfill(5)
		self.opcode = int(cmd[3:5])
		self.mode1 = OpcodeMode.POSITION if cmd[2] == '0' else OpcodeMode.IMMEDIATE
		self.mode2 = OpcodeMode.POSITION if cmd[1] == '0' else OpcodeMode.IMMEDIATE
		self.mode3 = OpcodeMode.POSITION if cmd[0] == '0' else OpcodeMode.IMMEDIATE

		self.output = None
		self.step = 0
		self.run = True
		if self.mode3 == OpcodeMode.IMMEDIATE:
			print('OpcodeMode.IMMEDIATE for parameter 3! {0}'.format(cmd))
			exit()

	def execute(self, tape, index, inputs):
		# print(self.opcode)
		if self.opcode == 1 or self.opcode == 2:
			self.step = 4
			p1 = tape[tape[index+1]] if self.mode1 == OpcodeMode.POSITION else tape[index+1]
			p2 = tape[tape[index+2]] if self.mode2 == OpcodeMode.POSITION else tape[index+2]
			if self.opcode == 1:
				result = p1+p2
			elif self.opcode == 2:
				result = p1*p2
			tape[tape[index+3]] = result
		elif self.opcode == 3:
			self.step = 2
			tape[tape[index+1]] = inputs[0]
			inputs = inputs[1:]
		elif self.opcode == 4:
			self.step = 2
			self.output = tape[tape[index+1]] if self.mode1 == OpcodeMode.POSITION else tape[index+1]
		elif self.opcode == 99:
			self.run = False
		else:
			print('Unexpected opcode {0}'.format(self.opcode))
			print(tape, index)
			exit()


def run_opcode(tape, index, inputs=[]):
	opcode = Opcode(tape, index)
	opcode.execute(tape, index, inputs)
	return opcode.run, opcode.step

def run_opcodes(tape, inputs=[]):
	outputs = []
	index = 0
	run = True
	while run:
		opcode = Opcode(tape, index)
		opcode.execute(tape, index, inputs)
		run = opcode.run
		index += opcode.step
		if opcode.output:
			outputs.append(opcode.output)
	return outputs
