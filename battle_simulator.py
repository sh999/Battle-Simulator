'''
Create simple battle simulator that can be extended for a bigger game
'''

from warrior import *	# Since I'm importing using wildcard, I'm using the modules as groupings of other modules
from die import *
from battlestats import *
from roundmanager import *

def game():
	'''
	'	Simulate damage with simple die mechanism
	'''
	myWarrior = Warrior("My warrior", 6, 5, 9)		# Create human and computer warriors
	compWarrior = Warrior("Computer warrior", 8, 4, 8)
	divider = "-" * 10
	battleStats = BattleStats(myWarrior, compWarrior)	# BattleStats keeps track of stats
	while myWarrior.getHealth() > 0 and compWarrior.getHealth() > 0:
	'''
	'	Loop battle while human warrior has positive health
	'''
		print divider
		myWarrior.printCondition()
		compWarrior.printCondition()
		attacker = determineAttacker(myWarrior, compWarrior)
		defender = determineDefender(attacker, myWarrior, compWarrior)
		damage = damageCalculator(attacker.getAttack(), defender.getDefense())
		defender.reduceHealth(damage)
		battleStats.addRounds()
		battleStats.recordDamage(myWarrior.getHealth(), compWarrior.getHealth())
		# a = raw_input()
	if myWarrior.getHealth() <= 0:				# Winning or losing scenario
		print myWarrior.getName(), "is dead!"
		battleStats.setWinner(compWarrior)
	else:
		print compWarrior.getName(), "is dead!"
		battleStats.setWinner(myWarrior)
	print divider
	
	print "Battle stats:"					# Display final result
	print "Winner = ", battleStats.getWinner()
	print "Total rounds = ", battleStats.getRounds()
	print "HP history = "
	print myWarrior.getName(), "  = ", battleStats.getHistory(myWarrior)
	print compWarrior.getName(), "= ", battleStats.getHistory(compWarrior)

game()
