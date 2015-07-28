'''
Create simple battle simulator that can be extended for a bigger game
'''

from warrior import *
from die import *
from battlestats import *
from roundmanager import *

def game():
	'''
	Simulate damage with simple die mechanism
	'''
	myWarrior = Warrior("My warrior", 6, 5, 9)
	compWarrior = Warrior("Computer warrior", 8, 4, 8)
	divider = "-" * 10
	battleStats = BattleStats(myWarrior, compWarrior)
	while myWarrior.getHealth() > 0 and compWarrior.getHealth() > 0:
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

game()