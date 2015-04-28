from die import *

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