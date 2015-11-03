import random
class DiceRoller():
	def __init__(self):
		self.Dice = [1,2,3,4,5,6]
		self.Roll = 0
		self.Roll1 = 0
		self.Roll2 = 0
		self.Roll3 = 0
		self.Roll4 = 0
		self.Roll5 = 0
		self.RollSum1 = 0
		self.RollSum2 = 0
		self.hrSum = []
		self.PokerSum = []
		self.GameChoice = True
		self.Player1Turn = True
		self.TwoPlayerGame = True
		self.Pause = ""
	def DiceRoll(self):
		self.Roll = random.choice(self.Dice)
		return self.Roll
	def ChoosePlayer(self):
                while self.TwoPlayerGame:
                        if self.Player1Turn == True:
                                print "First Player's turn"
                                self.Pause = raw_input()
                                self.PlayFullHousePoker()
                                self.Player1Turn = False
                        if self.Player1Turn == False:
                                print "Second Player's turn"
                                self.Pause = raw_input()
                                self.PlayFullHousePoker()
                                self.Player1Turn = True
                        else: user.InputSelection()
                        
	def PlayHighRollWins(self):
		self.DiceRoll()
		self.Roll1 = self.Roll
		self.DiceRoll()
		self.Roll2 = self.Roll
		self.RollSum1 = self.Roll1 + self.Roll2
		self.DiceRoll()
		self.Roll1 = self.Roll
		self.DiceRoll()
		self.Roll2 = self.Roll
		self.RollSum2 = self.Roll1 + self.Roll2
		if self.RollSum2 > self.RollSum1:
			print "Second Player Wins : " + str(self.RollSum2) + " > " + str(self.RollSum1)
			return
		if self.RollSum2 < self.RollSum1:
			print "First Player Wins" + str(self.RollSum1) + " > " + str(self.RollSum2)
			return 
		if self.RollSum1 == self.RollSum2:
			print "Tie Game, Roll Again" + str(self.RollSum1) + " = " + str(self.RollSum2)
			return
	def PlayFullHousePoker(self):
		self.Roll1 = random.choice(self.Dice)
		print str(self.Roll1)
		self.Roll2 = random.choice(self.Dice)
		print str(self.Roll2)
		self.Roll3 = random.choice(self.Dice)
		print str(self.Roll3)
		self.Roll4 = random.choice(self.Dice)
		print str(self.Roll4)
		self.Roll5 = random.choice(self.Dice)
		print str(self.Roll5)
		if self.Roll1 == self.Roll2 and self.Roll3 == self.Roll4 and self.Roll5:
			print "Full House"
			return
		if self.Roll1 == self.Roll3 and self.Roll2 == self.Roll4 and self.Roll5:
			print "Full House"
			return
		if self.Roll1 == self.Roll4 and self.Roll2 == self.Roll3 and self.Roll5:
			print "Full House"
			return
		if self.Roll1 == self.Roll5 and self.Roll2 == self.Roll3 and self.Roll4:
			print "Full House"
			return
		if self.Roll2 == self.Roll3 and self.Roll1 == self.Roll4 and self.Roll5:
			print "Full House"
			return
		if self.Roll2 == self.Roll4 and self.Roll1 == self.Roll3 and self.Roll5:
			print "Full House"
			return
		if self.Roll2 == self.Roll5 and self.Roll1 == self.Roll3 and self.Roll4:
			print "Full House"
			return
		if self.Roll3 == self.Roll4 and self.Roll1 == self.Roll2 and self.Roll5:
			print "Full House"
		if self.Roll3 == self.Roll5 and self.Roll1 == self.Roll2 and self.Roll4:
			print "Full House"
			return
		if self.Roll4 == self.Roll5 and self.Roll1 == self.Roll2 and self.Roll3:
			print "Full House"
			return
		if self.Roll1 == self.Roll2 and self.Roll3 and self.Roll4 and self.Roll1 != self.Roll5:
			print "Four of a kind : " + str(self.Roll1) + "'s"
			return
		if self.Roll1 == self.Roll2 and self.Roll3 and self.Roll5 and self.Roll1 != self.Roll4:
			print "Four of a kind : " + str(self.Roll1) + "'s"
			return
		if self.Roll1 == self.Roll2 and self.Roll4 and self.Roll5 and self.Roll1 != self.Roll3:
			print "Four of a kind : " + str(self.Roll1) + "'s"
			return
		if self.Roll1 == self.Roll3 and self.Roll4 and self.Roll5 and self.Roll1 != self.Roll2:
			print "Four of a kind : " + str(self.Roll1) + "'s"
			return
		if self.Roll2 == self.Roll3 and self.Roll4 and self.Roll5 and self.Roll2 != self.Roll1:
			print "Four of a kind : " + str(self.Roll2) + "'s"
			return
		if self.Roll1 == self.Roll2 and self.Roll3 and self.Roll1 != self.Roll4 and self.Roll5:
			print "Three of a kind : " + str(self.Roll1) + "'s"
			return
		if self.Roll1 == self.Roll2 and self.Roll4 and self.Roll1 != self.Roll3 and self.Roll5:
			print "Three of a kind : " + str(self.Roll1) + "'s"
			return
		if self.Roll1 == self.Roll2 and self.Roll5 and self.Roll1 != self.Roll3 and self.Roll4:
			print "Three of a kind : " + str(self.Roll1) + "'s"
			return
		if self.Roll2 == self.Roll3 and self.Roll4 and self.Roll2 != self.Roll1 and self.Roll5:
			print "Three of a kind : " + str(self.Roll2) + "'s"
			return
		if self.Roll2 == self.Roll3 and self.Roll5 and self.Roll2 != self.Roll1 and self.Roll4:
			print "Three of a kind : " + str(self.Roll2) + "'s"
			return
		if self.Roll2 == self.Roll4 and self.Roll5 and self.Roll2 != self.Roll1 and self.Roll3:
			print "Three of a kind : " + str(self.Roll2) + "'s"
			return
		if self.Roll3 == self.Roll4 and self.Roll5 and self.Roll3 != self.Roll1 and self.Roll2:
			print "Three of a kind : " + str(self.Roll3) + "'s"
			return
		if self.Roll1 == self.Roll2 and self.Roll1 != self.Roll3 and self.Roll4 and self.Roll5:
			print "Pair of "+ str(self.Roll1) + "'s"
			return
		if self.Roll1 == self.Roll3 and self.Roll1 != self.Roll2 and self.Roll4 and self.Roll5:
			print "Pair of "+ str(self.Roll1) + "'s"
			return
		if self.Roll1 == self.Roll4 and self.Roll1 != self.Roll2 and self.Roll3 and self.Roll5:
			print "Pair of "+ str(self.Roll1) + "'s"
			return
		if self.Roll1 == self.Roll5 and self.Roll1 != self.Roll2 and self.Roll3 and self.Roll4:
			print "Pair of "+ str(self.Roll1) + "'s"
			return
		if self.Roll2 == self.Roll3 and self.Roll2 != self.Roll1 and self.Roll4 and self.Roll5:
			print "Pair of "+ str(self.Roll2) + "'s"
			return
		if self.Roll2 == self.Roll4 and self.Roll2 != self.Roll1 and self.Roll3 and self.Roll5:
			print "Pair of "+ str(self.Roll2) + "'s"
			return
		if self.Roll2 == self.Roll5 and self.Roll2 != self.Roll1 and self.Roll3 and self.Roll4:
			print "Pair of "+ str(self.Roll2) + "'s"
			return
		if self.Roll3 == self.Roll4 and self.Roll3 != self.Roll1 and self.Roll2 and self.Roll5:
			print "Pair of "+ str(self.Roll3) + "'s"
			return
		if self.Roll3 == self.Roll5 and self.Roll3 != self.Roll1 and self.Roll2 and self.Roll4:
			print "Pair of "+ str(self.Roll3) + "'s"
			return
		if self.Roll4 == self.Roll5 and self.Roll4 != self.Roll1 and self.Roll2 and self.Roll3:
			print "Pair of "+ str(self.Roll4) + "'s"
			return
		else: 	
			print str(self.Roll1)
			print str(self.Roll2)
			print str(self.Roll3)
			print str(self.Roll4)
			print str(self.Roll5)
			return
	def InputSelection(self, input_var):
		while self.GameChoice:
			if input_var == 1:
				user.PlayHighRollWins()
				GameChoice = True
			if input_var == 2:
				user.PlayFullHousePoker()
				GameChoice = True
			if input_var == 3:
                                user.ChoosePlayer()
				GameChoice = False
			else: 
				input_var = input("Enter a number: ") 
				GameChoice = True
			
	
user = DiceRoller()
print "Welcome To Aaron's Dice Games"
print "If you would like to play High Roll press 1" 
print "If you would like to play Poker press 2"
print "If you would like to play a 2 player poker game press 3"
input_var = input("Enter a number: ") 
user.InputSelection(input_var)



			
		
				
			
			
			
			
			

	
