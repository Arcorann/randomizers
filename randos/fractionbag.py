import random

class Randomizer:
    def __init__(self, bag='jiltsoz',n=8):
        self.bag = bag
		self.whole,self.part = divmod(n,7)
        self.rebag()

    def rebag(self):
		self.pile = list(self.bag * self.whole)
		self.pile = self.pile + random.sample(list(self.bag),self.part)
        random.shuffle(self.pile)

    def next(self):
        p = self.pile.pop()
        if len(self.pile) == 0:
            self.rebag()
        return p
