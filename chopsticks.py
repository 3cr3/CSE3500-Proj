class Hand:
    def __init__(self, num_fingers=1):
        self.num_fingers = num_fingers
    
    def add(self, val):
        self.num_fingers = self.num_fingers + val if self.num_fingers + val < 5 else 0

class Player:
    def __init__(self, h1=Hand(), h2=Hand()):
        self.h1 = h1
        self.h2 = h2

    def add(self, hand, val):
        pass
    
    def split(self):
        pass
        
