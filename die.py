import random

class Die:
	'''
	Simple die simulator
	Can be rolled and give a random integer, and the maximum integer is set at object creation
	'''
	def __init__(self, maxNumber):
		self.maxNumber = maxNumber
		self.roll()

	def roll(self):
		self.rollNumber = random.randint(1, self.maxNumber)

	def getValue(self):
		return self.rollNumber