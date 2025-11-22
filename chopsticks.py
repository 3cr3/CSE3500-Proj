import sys
sys.setrecursionlimit(1000000)

class Hand:
    def __init__(self, num_fingers=1):
        self.num_fingers = num_fingers
    
    def add(self, val):
        self.num_fingers = (self.num_fingers + val) if self.num_fingers + val < 5 else 0

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
            return False
        return True
    
    def split(self, new_left, new_right):
        total = self.left.num_fingers + self.right.num_fingers
        # checks for legal split
        if new_left + new_right != total:
            return False
        if new_left >= 5 or new_right >= 5:
            return False
        if new_left == self.left.num_fingers or new_right == self.left.num_fingers:
            #this covers both the case that the hands haven't changed or have simply swapped 
            #if new_left is self.left.num_fingers, because total has been checked, new_right must 
            #also be self.right.num_fingers
            return False

        self.left.num_fingers = new_left
        self.right.num_fingers = new_right
        return True
    
class GameState:
    def __init__(self, p1=None, p2=None, is_p1_turn=True):
        self.p1 = p1 if p1 else Player()
        self.p2 = p2 if p2 else Player()
        self.is_p1_turn = is_p1_turn

    def is_terminal(self):
        # Checks if game is over
        p1_dead = (self.p1.left.num_fingers == 0 and
                   self.p1.right.num_fingers == 0)
        p2_dead = (self.p2.left.num_fingers == 0 and
                   self.p2.right.num_fingers == 0)
        return p1_dead or p2_dead

    def winner(self):
        """
        -1  -> Player 1 wins
        1 -> Player 2 wins
        0  -> Game not complete
        """
        if self.p2.left.num_fingers == 0 and self.p2.right.num_fingers == 0:
            return -1
        if self.p1.left.num_fingers == 0 and self.p1.right.num_fingers == 0:
            return 1
        return 0

    def copy(self):
        return GameState(
            Player(
                Hand(self.p1.left.num_fingers),
                Hand(self.p1.right.num_fingers)
            ),
            Player(
                Hand(self.p2.left.num_fingers),
                Hand(self.p2.right.num_fingers)
            ),
            self.is_p1_turn
        )
    
    def equals(self, other):
        return (self.p1.left.num_fingers == other.p1.left.num_fingers and
            self.p1.right.num_fingers == other.p1.right.num_fingers and
            self.p2.left.num_fingers == other.p2.left.num_fingers and
            self.p2.right.num_fingers == other.p2.right.num_fingers)
