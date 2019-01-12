"""
Fuck my life
This program is all about your fucked up life.
"""
class Fuck_Life(object):
	"""Multiple different functions to test out the fuck_life theory"""
	def __init__(self):
		super(Fuck_Life, self).__init__()
		print("Hello World")
		print('+++++========+++++====')
		print('======+++++======+++++')
		print('Fuck my life asshole!!!')

	def asshole(self):
		self.ass = int(input('How old are you?: '))
		self.hole = self.ass + 5
		print(f"In 5 years you will be {self.hole} years old")

	def fuckface(self):
		import random
		self.count = 0
		self.roll = random.randint(0,10)
		if self.roll < 5:
			print('you lose idiot')
		else:
			print('you win')
		while self.count == 0:
			lst = []
			for x in range(1,10):
				print(x)
			count == 1


                

a = Fuck_Life()
a.fuckface()
a.asshole()




