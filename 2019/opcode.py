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
		self.instruction = index
		self.run = True
		if self.mode3 == OpcodeMode.IMMEDIATE:
			print('OpcodeMode.IMMEDIATE for parameter 3! {0}'.format(cmd))
			exit()

	def execute(self, tape, inputs):
		# print(self.opcode)
		if self.opcode == 1 or self.opcode == 2:
			# addition p1+p2 or multiplication p1*p2 to p3 (always POSITION)
			p1 = tape[tape[self.instruction+1]] if self.mode1 == OpcodeMode.POSITION else tape[self.instruction+1]
			p2 = tape[tape[self.instruction+2]] if self.mode2 == OpcodeMode.POSITION else tape[self.instruction+2]
			if self.opcode == 1:
				result = p1+p2
			elif self.opcode == 2:
				result = p1*p2
			tape[tape[self.instruction+3]] = result
			self.instruction += 4

		elif self.opcode == 3:
			# read input to p1 (always POSITION)
			value = inputs.pop(0)
			tape[tape[self.instruction+1]] = value
			#print('Consumed input {0}, remaining: {1}'.format(value, inputs))
			self.instruction += 2

		elif self.opcode == 4:
			# write p1 to output (always POSITION)
			self.output = tape[tape[self.instruction+1]] if self.mode1 == OpcodeMode.POSITION else tape[self.instruction+1]
			#print('Produced output {0}'.format(self.output))
			self.instruction += 2

		elif self.opcode == 5 or self.opcode == 6:
			# 5: jump-if-true, if p1 is non-zero jump to p2
			# 6: jump-if-false, if p1 is zero jump to p2
			p1 = tape[tape[self.instruction+1]] if self.mode1 == OpcodeMode.POSITION else tape[self.instruction+1]
			p2 = tape[tape[self.instruction+2]] if self.mode2 == OpcodeMode.POSITION else tape[self.instruction+2]
			if self.opcode == 5 and p1 != 0:
				self.instruction = p2
			elif self.opcode == 6 and p1 == 0:
				self.instruction = p2
			else:
				self.instruction += 3

		elif self.opcode == 7 or self.opcode == 8:
			# 7: less-than, if p1 is less than p2, store 1 to p3, otherwise store 0
			# 8: equals, if p1 is equal to p2, store 1 to p3, otherwise store 0
			p1 = tape[tape[self.instruction+1]] if self.mode1 == OpcodeMode.POSITION else tape[self.instruction+1]
			p2 = tape[tape[self.instruction+2]] if self.mode2 == OpcodeMode.POSITION else tape[self.instruction+2]
			result = 0
			if self.opcode == 7 and p1 < p2:
				result = 1
			elif self.opcode == 8 and p1 == p2:
				result = 1
			tape[tape[self.instruction+3]] = result
			self.instruction += 4

		elif self.opcode == 99:
			self.run = False

		else:
			print('Unexpected opcode {0}'.format(self.opcode))
			print(tape, self.instruction)
			exit()


def run_opcode(tape, instruction, inputs=[]):
	opcode = Opcode(tape, instruction)
	opcode.execute(tape, inputs)
	return opcode.run, opcode.instruction

def run_opcodes(tape, inputs=[]):
	outputs = []
	instruction = 0
	run = True
	while run:
		opcode = Opcode(tape, instruction)
		opcode.execute(tape, inputs)
		run = opcode.run
		instruction = opcode.instruction
		if opcode.output:
			outputs.append(opcode.output)
	return outputs
