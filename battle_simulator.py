'''
Create simple battle simulator that can be extended for a bigger game
Simulator mechanics can be as simple as dice-based or 
'''

import random

class Warrior():
	def __init__(self, attack, defense, agility):
		self.attack = attack
		self.defense = defense
		self.agility = agility
		self.health = 30

	def getAttack(self):
		return self.attack

	def getDefense(self):
		return self.defense

	def getAgility(self):
		return self.agility

	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name

	def getHealth(self):
		return self.health

	def reduceHealth(self,points):
		self.health -= points

class Die:
	def __init__(self, maxNumber):
		self.maxNumber = maxNumber
		self.roll()

	def roll(self):
		self.rollNumber = random.randint(1, self.maxNumber)

	def getValue(self):
		return self.rollNumber

def damageCalculator(dieMax1, dieMax2):
	'''
	Uses Die objects to calculate damage
	'''
	die1 = Die(dieMax1)
	die1.getValue()
	die2 = Die(dieMax2)
	die2.getValue()
	damage = die1.getValue() - die2.getValue()
	if damage < 0: # Disallows negative damage
		damage = 0
	print "damage = ", damage
	return damage

def determineAttacker(warrior1, warrior2):
	'''
	Whoever has the higher agility roll attacks first
	'''
	die1 = Die(warrior1.getAgility())
	die2 = Die(warrior2.getAgility())
	diff = die1.getValue() - die2.getValue()

	while diff == 0:
		die1.roll()
		die2.roll()
		diff = die1.getValue() - die2.getValue()
	if diff > 0:
		print warrior1.getName(), "attacks"
		attacker = warrior1
	elif diff < 0:
		print warrior2.getName(), "attacks"
		attacker = warrior2
	return attacker

def determineDefender(attacker,warrior1,warrior2):
	if attacker == warrior1:
		defender = warrior2
	else:
		defender = warrior1
	return defender

def printCondition(warrior):
	print warrior.getName(), "HP =", warrior.getHealth()

class BattleStats:
	def __init__(self, warrior1, warrior2):
		self.warrior1 = warrior1
		self.warrior2 = warrior2
		self.totalRounds = 0
		self.warrior1health = [warrior1.getHealth()]
		self.warrior2health = [warrior2.getHealth()]
	def addRounds(self):
		self.totalRounds += 1
	def getRounds(self):
		return self.totalRounds
	def setWinner(self, warrior):
		self.winner = warrior
	def getWinner(self):
		return self.winner.getName()
	def recordDamage(self, w1Health, w2Health):
		self.warrior1health.append(w1Health)
		self.warrior2health.append(w2Health)
	def getHistory(self, warrior):
		if warrior == self.warrior1:
			return self.warrior1health
		else:
			return self.warrior2health

def battleWithDice():
	'''
	Simulate damage with simple die mechanism
	'''
	myWarrior = Warrior(6, 5, 9)
	compWarrior = Warrior(8, 4, 8)
	myWarrior.setName("My warrior");
	compWarrior.setName("Computer warrior");
	divider = "-" * 10
	battleStats = BattleStats(myWarrior, compWarrior)
	while myWarrior.getHealth() > 0 and compWarrior.getHealth() > 0:
		print divider
		printCondition(myWarrior)
		printCondition(compWarrior)
		attacker = determineAttacker(myWarrior, compWarrior)
		defender = determineDefender(attacker, myWarrior, compWarrior)
		damage = damageCalculator(attacker.getAttack(), defender.getDefense())
		defender.reduceHealth(damage)
		battleStats.addRounds()
		battleStats.recordDamage(myWarrior.getHealth(), compWarrior.getHealth())
		a = raw_input()
	if myWarrior.getHealth() <= 0:
		print myWarrior.getName(), "is dead!"
		battleStats.setWinner(compWarrior)
	else:
		print compWarrior.getName(), "is dead!"
		battleStats.setWinner(myWarrior)
	print divider
	print "Battle stats:"
	print "Winner = ", battleStats.getWinner()
	print "Total rounds = ", battleStats.getRounds()
	print "HP history = "
	print myWarrior.getName(), "  = ", battleStats.getHistory(myWarrior)
	print compWarrior.getName(), "= ", battleStats.getHistory(compWarrior)

battleWithDice()