#!/usr/bin/env python

data = """Faerun to Tristram = 65
Faerun to Tambi = 129
Faerun to Norrath = 144
Faerun to Snowdin = 71
Faerun to Straylight = 137
Faerun to AlphaCentauri = 3
Faerun to Arbre = 149
Tristram to Tambi = 63
Tristram to Norrath = 4
Tristram to Snowdin = 105
Tristram to Straylight = 125
Tristram to AlphaCentauri = 55
Tristram to Arbre = 14
Tambi to Norrath = 68
Tambi to Snowdin = 52
Tambi to Straylight = 65
Tambi to AlphaCentauri = 22
Tambi to Arbre = 143
Norrath to Snowdin = 8
Norrath to Straylight = 23
Norrath to AlphaCentauri = 136
Norrath to Arbre = 115
Snowdin to Straylight = 101
Snowdin to AlphaCentauri = 84
Snowdin to Arbre = 96
Straylight to AlphaCentauri = 107
Straylight to Arbre = 14
AlphaCentauri to Arbre = 46"""

class Node:
	def __init__(self, name):
		self.name = name
		self.edges = {}

	def add_edge(self, other, distance):
		self.edges[other] = distance

	def distance_to(self, other):
		return self.edges[other]

	def __repr__(self):
		s = '<Node: {0}>'.format(self.name)
		return s

class Graph:
	def __init__(self):
		self.nodes = {}

	def add_edge(self, one, two, distance):
		if one not in self.nodes:
			self.nodes[one] = Node(one)
		if two not in self.nodes:
			self.nodes[two] = Node(two)

		self.nodes[one].add_edge(two, distance)
		self.nodes[two].add_edge(one, distance)

	def __repr__(self):
		s = '<Graph: '
		for k, n in self.nodes.items():
			s += repr(n) + ' '
		s += '>'
		return s

	def traverse(self, visited=[]):

		if len(visited) == len(self.nodes):
			# calculate the distance for this route
			d = 0
			for i in range(len(visited)-1):
				d += visited[i].distance_to(visited[i+1].name)
			return d, d
		else:
			shortest = -1
			longest = 0

			# traverse all possible next nodes, avoiding visited nodes
			for name, node in self.nodes.items():
				if node in visited:
					continue

				visited.append(node)
				s, l = self.traverse(visited)
				visited.pop(len(visited) - 1)

				if shortest < 0 or s < shortest:
					shortest = s
				longest = max(longest, l)

			return shortest, longest


g = Graph()

lines = data.split('\n')
for line in lines:
	words = line.split(' ')
	a, b, d = words[0], words[2], int(words[4])
	g.add_edge(a, b, d)

shortest, longest = g.traverse()
print(shortest)
print(longest)