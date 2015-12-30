"""
Word Jumble
------------
A welcoming screen will pop up which explains the rules.
The user will be given three chances to decypher a
scrambled word. If the word is too difficult, the user
will be allowed one "pass". The user's score will be
recorded by adding the number of letters they decyphered.
At the end of the game, the score will be displayed and
the user will be given the opportunity to play again.
"""

import random
import urllib		

class Words(object):

	def __init__(self):
		
		wordurl = urllib.urlopen('http://www-01.sil.org/linguistics/wordlists/english/wordlist/wordsEn.txt')
		self.words = []
		
		for word in wordurl.readlines():
			self.words.append(word.strip())
		
	def get(self):
		return self.words[random.randint(0, len(self.words)-1)]
		
	def scramble(self, word):
		
		# convert string to list of characters for scrambling
		chars = []
		x = range(0,len(word))
		for i in x:
			chars.append(word[i])
		
		# scrambles the characters
		chars_scrambled = []
		while len(x) != 0:
			chars_scrambled.append(chars[x.pop(random.randint(0, len(x)-1))])
			
		return ''.join(chars_scrambled)	

class Engine(object):

	def __init__(self, Words):
		self.words = Words
		
	def play(self):
	
		# Shows opening screen with rules
		print "Welcome to Word Jumble.\n"
		print "\tYou have three chances to unscramble a word correctly."
		print "\tScores are proportional to word length. The higher"
		print "\tyour streak, the higher your score. If you use"
		print "\tall three chances, then it's game over. You'll also be"
		print "\tbe given one 'pass' if you would like to skip a word."
		print "\tYou may pass a word once by typing in 'pass'.\n\n"
		
		chances = 3
		passes = 1
		score = 0
		correct = 0
		
		answer = self.words.get()
		scramble = self.words.scramble(answer)
		
		print "The scrambled word is: %s" % scramble 
		
		while chances != 0:
			
			print "You have %d chance(s) left." % chances
			input = raw_input("\nUnscramble the word >> ")
			
			if input == answer:
				correct += 1
				points = len(answer) * correct
				print "Correct! You earned %d points." % points
				score += points
				
				answer = self.words.get()
				scramble = self.words.scramble(answer)
				print "\nThe scrambled word is: %s" % scramble
				chances = 3
			elif input == 'pass':
				if passes != 0:
					passes -= 1
					print "You've chosen to pass on this word.\n"
					answer = self.words.get()
					scramble = self.words.scramble(answer)
					chances = 3
					print "The new scrambled word is: %s" % scramble
				else:
					print "You have no passes left!"
			else:	
				chances -= 1
					
		return score
		
	def playagain(self):
		
		while True:
			input = raw_input("\nWould you like to play again? >> ")
			
			if input == 'yes':
				return input
			elif input == 'no':
				return input
			else:
				print "Please enter either 'yes' or 'no'."
			
# sets the game up		
game = Engine(Words())

# enters the game loop
playagain = 'yes'
while playagain != 'no':
	score = game.play()
	print '-' * 30
	
	if score > 0:
		print "Congratulations! You scored %d!" % score
	else:
		print "You lost! Better luck next time."
		
	playagain = game.playagain()
	print "-" * 30
	print "\n"
	
print "Thanks for playing!"		