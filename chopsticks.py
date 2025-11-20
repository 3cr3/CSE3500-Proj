class Hand:
    def __init__(self, num_fingers=1):
        self.num_fingers = num_fingers
    
    def add(self, val):
        self.num_fingers = self.num_fingers + val if self.num_fingers + val < 5 else 0

class Player:
    def __init__(self, left=None, right=None):
        self.left = left if left else Hand()
        self.right = right if right else Hand()

    def add(self, target_hand, val):
        if target_hand.upper() == "L" and self.left.num_fingers > 0:
            self.left.add(val)
        elif target_hand.upper() == "R" and self.right.num_fingers > 0:
            self.right.add(val)
        else:
            print("invalid target")
    
    def split(self, new_left, new_right):
        total = self.left.num_fingers + self.right.num_fingers
        # checks for legal split
        if new_left + new_right != total:
            return False
        if new_left >= 5 or new_right >= 5:
            return False
        if new_left == self.left.num_fingers or new_right == self.left.num_fingers:
            return False

        self.left.num_fingers = new_left
        self.right.num_fingers = new_right
        return True
    
