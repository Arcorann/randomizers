import random

class Randomizer:
	# this should probably get its own class so we can vary weights and initial history, but I don't know what to call it
	weights = [6,5,4,3,2,1,0]
	
	def __init__(self):
		self.hist = list('ijltozs') # 0562134, where 0123456 = 'iotzsjl'

	def next(self):
		# we could use random.choices here, but that's only in 3.6
		# i = random.choices(range(0,len(self.weights)),weights=self.weights)
		w = random.randint(0, sum(self.weights) - 1)
		i = -1
		while w >= 0:
			i += 1
			w -= weights[i]
		p = self.hist.pop(i)
		self.hist.append(i)
		return p