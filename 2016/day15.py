#!/usr/bin/env python

data = """Sprinkles: capacity 5, durability -1, flavor 0, texture 0, calories 5
PeanutButter: capacity -1, durability 3, flavor 0, texture 0, calories 1
Frosting: capacity 0, durability -1, flavor 4, texture 0, calories 6
Sugar: capacity -1, durability 0, flavor 0, texture 2, calories 8"""

class RecipeGenerator():
	def __init__(self, count, total):
		self.count = count
		self.total = total
		self.current = None

	def __iter__(self):
		return self

	def _increment(self):
		if self.current == None:
			self.current = [self.total]
			self.current.extend([0] * (self.count - 1))
		else:
			if self.current[0] > 0:
				# simply decrement the first number, increment the second
				self.current[0] -= 1
				self.current[1] += 1
			elif self.current[-1] < self.total:
				# time to roll a value over to the right
				# find the index of the first non-zero value
				index = 0
				while self.current[index] == 0:
					index += 1
				if self.current[index+1] < self.total:
					# if this number can be incremented, do it and reset the one before it
					self.current[index+1] += 1
					self.current[index] = 0
				else:
					# otherwise, set it back to zero and roll to the right
					self.current[index+1] = 0
					self.current[index+2] = 1
				# reset the first number back to the remainder of the other numbers in the tuple
				self.current[0] = self.total - sum(self.current[1:])
			else:
				# finished, stop iterating
				self.current = None

		return self.current

	def next(self):
		item = self._increment()
		if item == None:
			raise StopIteration
		else:
			return tuple(item)


class Ingredient():
	def __init__(self, name, capacity, durability, flavor, texture, calories):
		self.name = name
		self.capacity = capacity
		self.durability = durability
		self.flavor = flavor
		self.texture = texture
		self.calories = calories

	def __repr__(self):
		return '<Ingredient "{0}", cap {1}, dur {2}, fla {3}, tex {4}, cal {5}'.format(self.name, self.capacity, self.durability, self.flavor, self.texture, self.calories)

class IngredientMixer():
	def __init__(self):
		self.ingredients = []

	def add_ingredient(self, ingredient):
		self.ingredients.append(ingredient)

	def _score_recipe(self, recipe):
		fields = ['capacity', 'durability', 'flavor', 'texture']

		capacity = 0
		durability = 0
		flavor = 0
		texture = 0
		for index, ingredient in enumerate(self.ingredients):
			capacity += (recipe[index] * ingredient.capacity)
			durability += (recipe[index] * ingredient.durability)
			flavor += (recipe[index] * ingredient.flavor)
			texture += (recipe[index] * ingredient.texture)

		capacity = max(capacity, 0)
		durability = max(durability, 0)
		flavor = max(flavor, 0)
		texture = max(texture, 0)

		return capacity * durability * flavor * texture

	def _count_calories(self, recipe):
		calories = 0
		for index, ingredient in enumerate(self.ingredients):
			calories += (recipe[index] * ingredient.calories)
		calories = max(calories, 0)
		return calories

	def find_optimal_recipe(self, teaspoons, calories=None):
		optimal = None
		biggest = 0

		rg = RecipeGenerator(len(self.ingredients), teaspoons)
		for recipe in rg:

			if calories != None:
				if self._count_calories(recipe) != calories:
					continue

			score = self._score_recipe(recipe)
			if score > biggest:
				optimal = recipe
				biggest = score

		return optimal, biggest



im = IngredientMixer()

lines = data.split('\n')
for line in lines:
	words = line.split(' ')
	i = Ingredient(words[0][:-1], int(words[2][:-1]), int(words[4][:-1]), int(words[6][:-1]), int(words[8][:-1]), int(words[10]))
	im.add_ingredient(i)

recipe, score = im.find_optimal_recipe(100)
print recipe, score

recipe, score = im.find_optimal_recipe(100, calories=500)
print recipe, score