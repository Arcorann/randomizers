import random

class Randomizer:
    def __init__(self, bag='jiltsoz',n=6):
        self.bag = bag
		self.bagsize = n
        self.rebag()

    def rebag(self):
        self.pile = random.sample(list(self.bag),self.bagsize)

    def next(self):
        p = self.pile.pop()
        if len(self.pile) == 0:
            self.rebag()
        return p
