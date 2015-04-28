import random

class Die:
	def __init__(self, maxNumber):
		self.maxNumber = maxNumber
		self.roll()

	def roll(self):
		self.rollNumber = random.randint(1, self.maxNumber)

	def getValue(self):
		return self.rollNumber