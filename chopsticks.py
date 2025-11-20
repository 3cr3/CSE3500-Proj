class Hand:
    def __init__(self, num_fingers=1):
        self.num_fingers = num_fingers
    
    def add(self, val):
        self.num_fingers = self.num_fingers + val if self.num_fingers + val < 5 else 0

class Player:
    def __init__(self, left=Hand(), right=Hand()):
        self.left = left
        self.right = right

    def add(self, target_hand, val):
        if target_hand.upper() == "L" and self.left > 0:
            self.left.add(val)
        elif target_hand.upper() == "R" and self.right > 0:
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
        if new_left == self.left or new_right == self.left:
            return False

        self.left.num_fingers = new_left
        self.right.num_fingers = new_right
        return True
    
