#!/usr/bin/env python

data = """
Rudolph can fly 22 km/s for 8 seconds, but then must rest for 165 seconds.
Cupid can fly 8 km/s for 17 seconds, but then must rest for 114 seconds.
Prancer can fly 18 km/s for 6 seconds, but then must rest for 103 seconds.
Donner can fly 25 km/s for 6 seconds, but then must rest for 145 seconds.
Dasher can fly 11 km/s for 12 seconds, but then must rest for 125 seconds.
Comet can fly 21 km/s for 6 seconds, but then must rest for 121 seconds.
Blitzen can fly 18 km/s for 3 seconds, but then must rest for 50 seconds.
Vixen can fly 20 km/s for 4 seconds, but then must rest for 75 seconds.
Dancer can fly 7 km/s for 20 seconds, but then must rest for 119 seconds.
"""

class Reindeer:
	def __init__(self, name, speed, fly_time, rest_time):
		self.name = name
		self.speed = speed
		self.fly_time = fly_time
		self.rest_time = rest_time

		self.time = 0
		self.is_flying = True
		self.time_since_takeoff = 0
		self.distance = 0

		self.score = 0

	def __repr__(self):
		return '<{0} - {1} km - {2} pts>'.format(self.name, self.distance, self.score)

	def pass_one_second(self):
		if self.is_flying:
			self.distance = self.distance + self.speed

		self.time = self.time + 1
		self.time_since_takeoff = self.time_since_takeoff + 1

		if self.is_flying:
			if self.time_since_takeoff == self.fly_time:
				self.is_flying = False
				self.time_since_takeoff = 0

		elif not self.is_flying:
			if self.time_since_takeoff == self.rest_time:
				self.is_flying = True
				self.time_since_takeoff = 0

class ReindeerHolder():
	def __init__(self, reindeer):
		self.reindeer = reindeer

	def _pass_one_second(self):
		furthest = []
		for r in self.reindeer:
			r.pass_one_second()
			if len(furthest) == 0:
				furthest.append(r)
			elif r.distance == furthest[0].distance:
				furthest.append(r)
			elif r.distance > furthest[0].distance:
				furthest = [r]

		for r in furthest:
			r.score = r.score + 1

	def pass_seconds(self, count):
		for seconds in range(count):
			self._pass_one_second()

	def get_reindeer_with_highest_score(self):
		scoriest = self.reindeer[0]
		for r in self.reindeer:
			if r.score > scoriest.score:
				scoriest = r
		return scoriest

	def get_furthest_reindeer(self):
		furthest = self.reindeer[0]
		for r in self.reindeer:
			if r.distance > furthest.distance:
				furthest = r
		return furthest


def load_reindeer(reindeer_data):
	lines = reindeer_data.strip().split('\n')
	reindeer = []

	for line in lines:
		words = line.split(' ')

		name = words[0]
		speed = int(words[3])
		fly_time = int(words[6])
		rest_time = int(words[13])

		r = Reindeer(name, speed, fly_time, rest_time)
		reindeer.append(r)

	return reindeer


def solve_part_1():

	reindeer = load_reindeer(data)

	rh = ReindeerHolder(reindeer)
	rh.pass_seconds(2503)

	furthest = rh.get_furthest_reindeer()
	print(furthest)

	# should be Cupid at 2696 km


def solve_part_2():

	reindeer = load_reindeer(data)

	rh = ReindeerHolder(reindeer)
	rh.pass_seconds(2503)

	best = rh.get_reindeer_with_highest_score()
	print(best)

solve_part_1()
solve_part_2()