'''class tracks who's turn it is (ai computer or human)'''
class GameState:

    def __init__(self, p1, p2, is_p1_turn = True):
        self.p1 = p1
        self.p2 = p2
        self.is_p1_turn = is_p1_turn

    def is_terminal(self): '''check if game over'''
        p1_dead = self.p1.left.num_fingers == 0 and self.p1.right.num_fingers == 0 #p1 dead
        p2_dead = self.p2.left.num_fingers == 0 and self.p2.right.num_fingers == 0 #p2 dead
        return p1_dead or p2_dead
    
    def winner(self):
        #1 if p1 wins, -1 if p2 wins, 0 if no winner (yet)
        if self.p1.left.num_fingers == 0 and self.p1.right.num_fingers == 0:
            return -1
        if self.p2.left.num_fingers == 0 and self.p2.right.num_fingers == 0:
            return -1
        return 0
    
    def copy(self):
        from chopsticks import Player, Hand
        p1_copy = Player(Hand(self.p1.left.num_fingers), Hand(self.p1.right.num_fingers))
        p2_copy = Player(Hand(self.p2.left.num_fingers), Hand(self.p2.right.num_fingers))
        return GameState(p1_copy, p2_copy, self.is_p1_turn)



def minimax():

def getbestmove():

def apply_move():