class Warrior():
	'''
	Barebones class that is meant to have a warrior's stats
	Not intended to have complex methods that have calculations and heavy logic
	'''
	def __init__(self, name, attack, defense, agility):
		self.attack = attack
		self.defense = defense
		self.agility = agility
		self.health = 30
		self.name = name

	def getAttack(self):
		return self.attack

	def getDefense(self):
		return self.defense

	def getAgility(self):
		return self.agility

	def getName(self):
		return self.name

	def getHealth(self):
		return self.health

	def reduceHealth(self,points):
		self.health -= points

	def printCondition(self):
		print self.name, "HP =", self.health