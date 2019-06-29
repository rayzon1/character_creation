"""
This program is one of my small beginner projects.
"""
class PrimaryClass (object):
	"""Multiple different functions to test"""
	def __init__(self):
		print("Hello World")
		print('+++++========+++++====')
		print('======+++++======+++++')
		print('Welcome to my App!')

	def promptAge(self):
		self.prompt = int(input('How old are you?: '))
		self.addFive = self.prompt + 5
		print(f"In 5 years you will be {self.addFive} years old")

	def randomRoll(self):
		import random
		self.roll = random.randint(0,10)
		if self.roll < 5:
			print('you lose')
		else:
			print('you win')
			


                

a = PrimaryClass()
a.promptAge()
a.randomRoll()




