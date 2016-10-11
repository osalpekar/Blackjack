import random

#outline the player Class
class Player():

	#simulating a suit where 1 reps ace and 11-13 rep jack, queen, and king respectively
	deck = [i for i in range(1,14)]
	#frequency_deck maps cards to the number of those left in the deck
	frequency_deck = {'2': 4, '3':4, '4':4, '5':4, '6':4, '7':4, '8':4, '9':4, '10':4, \
						'ace':4, 'jack':4, 'queen':4, 'king':4} 
	
	def __init__(self, name):
		self.name = name
		self.hand = [] #list of cards in hand as strings
		self.value_hand = [] #list of values of cards in hand
		self.score = 0
		self.active = True
	
	#prints out the player's hand
	def display_hand(self):
		print('Your hand is currently: ' + str(self.hand))
	
	#what to do if user wants to hit
	def hit(self):
		card = random.choice(Player.deck)
		value = 0

		#Displaying the card that has been dealt
		temp_string = ''
		if card == 13:
			temp_string = 'king'
			value = 10
		elif card == 12:
			temp_string = 'queen'
			value = 10
		elif card == 11:
			temp_string = 'jack'
			value = 10
		elif card == 1:
			temp_string = 'ace'
			value = 100 #placeholder for ace
		else:
			temp_string = str(card)
			value = card
		print('You have been dealt a ' + temp_string)
		
		#handling if all cards of certain type have been dealt from hand
		Player.frequency_deck[temp_string] -= 1
		if Player.frequency_deck[temp_string] == 0:
			del Player.frequency_deck[temp_string]
			Player.deck.remove(card)
		
		#adding to the hand and optimizing the value
		self.hand.append(temp_string)
		self.value_hand.append(value)
		self.optimize()
	
	#what to do if user wants to stay
	def stay(self):
		print('You have completed playing')
		print('Your current hand is ' + str(self.hand))
		print('Your current score is ' + str(self.score))
		self.active = False
	
	#algorithm to optimize the use of the ace card(s) in the user's hand
	def optimize(self):
		counter = 0
		for item in self.value_hand:
			if item == 100:
				counter += 1
		
		if 100 in self.value_hand:
			#aces present in hand
			i = 0
			self.score = sum(self.value_hand) - (100 * counter)

			#accounting for fact that there may be multiple aces in hand
			while (i < counter):
				add_eleven = self.score + 11
				add_one= self.score + 1

				#using cases to determine whether 11 or 1 is more advantageous
				if add_one > 21:
					self.score = add_one
				elif add_one < 21 and add_eleven > 21:
					self.score = add_one
				else:
					option1 = 21 - add_eleven
					option2 = 21 - add_one
					if option1 < option2:
						self.score = add_eleven
					else:
						self.score = add_one
				i += 1
		else:
			#if no aces in hand
			self.score = sum(self.value_hand)

