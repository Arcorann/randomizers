import bag

class Randomizer(bag.Randomizer):
    def __init__(self):
        bag.Randomizer.__init__(self, 'jiltsoz'*9)
