#IMPORTS
import random

#VARIBLE DEFININTIONS
class deck:
	"""Deck of Cards"""
	def __init__(self, length=0):
		self.length = length
		self.cards = []
		self.lastAccess = 0
		self.value = [0,0]
		self.aceH = True
		for i in range (length):
			self.cards.append(i+1)

	def shuffle(self):
		print("Shuffling the deck...")
		#None -> None
		random.shuffle(self.cards)
		self.lastAccess = 0

	def hit(self,stack):
		#Deck -> None
		self.cards.append(stack.cards[stack.lastAccess])
		self.score(stack.cards[stack.lastAccess])
		stack.lastAccess += 1

	def clear(self):
		self.cards = []
		self.value = [0,0]

	def score(self,card):
		if((card%13)<=10 and ((card%13) > 1)):
			if(not(self.value[1])):
				self.value[0] += card%13
			else:
				self.value[0] += card%13
				self.value[1] += card%13
		elif((card%13 == 0) or (card%13 == 11) or (card%13 == 12)):
			if(not(self.value[1])):
				self.value[0] += 10
			else:
				self.value[0] += 10
				self.value[1] += 10
		else:
			if(self.aceH):
				self.value[1] = self.value[0] + 1
				self.value[0] += 11
				self.aceH = False
			else:
				self.value[1] += 1
				self.value[0] += 1

class Bank:
	"""Bank"""
	def __init__(self, total):
		self.total = total
		self.current = 0
		self.ibet = 0

	def bet(self):
		while True:
			while True:
				try:
					self.current = int(raw_input("Current Total: " + str(self.total) + " \n Place your bets! "))
					break
				except ValueError:
					print "Oops!  That was not a valid number.\nYour value must be greater than zero.\nTry again..."
			if(self.current > 0 and self.current <= self.total):
				self.total -= self.current
				break

	def lose(self):
		self.current = 0
		self.total += 2*self.ibet
		self.ibet = 0
		print "You lost!\nDealer is laughing at you.\nTry again and take him down a notch."
		fold()
	def win(self):
		self.total += 2*self.current
		self.current = 0
		self.ibet = 0
		print "VICTORY!!!!\nDealer ain't got nothing on you."
		fold()
	def push(self):
		self.total += self.current
		self.current = 0
		self.ibet = 0
		print "Push!\nDealer got lucky. Let\'s get him next time."
		fold()


	def insurance(self):
		while True:
			while True:
				try:
					self.ibet = int(raw_input("The dealer is showing an ace.\nHow much insurance would you like?\nCurrent Bet: " + str(self.current) + "\nCurrent Total:" + str(self.total) + "\n"))
					break
				except ValueError:
					print "Oops!  That was not a valid number.\nYour value must be either nonnegative integer.\nTry again..."
			if(self.ibet >= 0 and self.ibet < self.total and self.ibet <= self.current/2):
				break
			else:
				print "Insurance must be either zero or up to half your current bet."
	def blackjack():
		self.total += 3*self.current
		self.current = 0
		self.ibet = 0
		print "BLACKJACK!!!!!!!!!!!\nWe got a high-roller over here!"
		fold()
mainDeck = deck(52) 
hand = deck()
dealer = deck()
bank = Bank(10000)
#GLOBAL VARIABLES
convertor = [" K", "n A", " 2", " 3", " 4", " 5"," 6"," 7","n 8"," 9"," 10"," J"," Q"]
converter = ["Spades","Hearts","Clubs","Diamonds"]
#FUNCTION DEFINITIONS
def fold():
	if(bank.total<=0):
		print "GAME OVER YOU LAZY BROKE"
		return False
	else:
		mainDeck.shuffle()
		hand.clear()
		dealer.clear()
		bank.bet()
		hand.hit(mainDeck)
		hand.hit(mainDeck)
		dealer.hit(mainDeck)
		dealer.hit(mainDeck)
		iblackjack()

def stay(val1=0,index=0):
	if(index==0):
		if(dealer.value[0]>=17):
			if(dealer.value[0]>21):
				stay(val1,1)
			else:
				compare(val1,0)
		else:

			dealer.hit(mainDeck)
			a = []
			b = []
			for card in dealer.cards:
				a.append(convertor[card%13])
				b.append(converter[card%4])
			print "The dealer now has:\na%s of %s" % (a[0],b[0])
			if(len(a)>1):
				for i in range(1,len(a)):
					print "and a%s of %s" % (a[i],b[i])

			stay(val1,0)
	elif(index==1):
		if(dealer.value[1]>=17 or dealer.value[1] == 0):
			if(dealer.value[1]>21 or dealer.value[1] == 0):
				bank.win()
			else:
				compare(val1,1)
		else:
			dealer.hit(mainDeck)
			stay(val1,1)

def compare(val1=0,val2=0):
	if(hand.value[val1]>dealer.value[val2]):
		bank.win()
	elif(hand.value[val1]<dealer.value[val2]):
		bank.lose()
	else:
		bank.push()

def iblackjack():
	if(hand.value[0]==21):
		if(dealer.value[0]==21):
			bank.push()
		else:
			bank.blackjack()
	if(dealer.cards[1]%13 == 1):
		bank.insurance()
		if(dealer.value[0] == 21):
			bank.lose()
		else:
			bank.ibet=0
			hit_stay(0)
	else:
		hit_stay(0)

def hitFlow():
	hand.hit(mainDeck)
	if(hand.value[0] > 21):
		if(hand.value[1] > 21 or hand.value[1] <= 0):
			bank.lose()
		else:
			hit_stay(1)
	else:
		hit_stay(0)


def hit_stay(index=0):
	a = []
	b = []
	
	for card in hand.cards:
		a.append(convertor[card%13])
		b.append(converter[card%4])

	print "You now have:\na%s of %s" % (a[0],b[0])
	if(len(a)>1):
		for i in range(1,len(a)):
			print "and a%s of %s" % (a[i],b[i])

	print "The dealer has a%s of %s." % (convertor[dealer.cards[1]%13],converter[dealer.cards[1]%4])
	while True:
		ans = str(raw_input("Would you like to hit or stay?: "))
		if (ans.lower() == "hit" or ans.lower() == "h" or ans.lower() == "stay" or ans.lower() == "s"):
			break
	if (ans.lower() == "hit" or ans.lower() == "h"):
		print "Hit me brah!"
		hitFlow()
	if (ans.lower() == "stay" or ans.lower() == "s"):
		print "I'm g with what I got."
		a = []
		b = []
		for card in dealer.cards:
			a.append(convertor[card%13])
			b.append(converter[card%4])
		print "The dealer now has:\na%s of %s" % (a[0],b[0])
		if(len(a)>1):
			for i in range(1,len(a)):
				print "and a%s of %s" % (a[i],b[i])
		stay()

#MAIN CODE
fold()
