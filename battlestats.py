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