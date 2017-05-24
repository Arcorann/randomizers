import random

class Randomizer:
    def __init__(self, bag='jiltsoz',n=6):
        self.bag = bag
        self.rebag(n)

    def rebag(self,n):
        self.pile = list(self.bag)
        random.shuffle(self.pile)
		self.pile = self.pile[0:(n-1)]

    def next(self):
        p = self.pile.pop()
        if len(self.pile) == 0:
            self.rebag(n)
        return p
