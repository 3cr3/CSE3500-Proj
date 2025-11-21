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
        1  -> Player 1 wins
        -1 -> Player 2 wins
        0  -> Game not complete
        """
        if self.p2.left.num_fingers == 0 and self.p2.right.num_fingers == 0:
            return 1
        if self.p1.left.num_fingers == 0 and self.p1.right.num_fingers == 0:
            return -1
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

if __name__ ==  '__main__':
    place = input("Welcome to chopsticks! Would you like to go first or second? (F/S)").upper()
    while place not in {'F', 'S'}:
        place = input("Please input F for first and S for second.").upper()

    if place.upper() == 'F':
        game = GameState(is_p1_turn=True)
    else:
        game = GameState(is_p1_turn=False)

    while not game.is_terminal():
        print(f"\nYour left hand has {game.p1.left.num_fingers}  and your right hand has {game.p1.right.num_fingers} ")
        print(f"Your opponent's left hand has {game.p2.left.num_fingers}  and their left hand has {game.p2.right.num_fingers} \n")
        if game.is_p1_turn:
            #Switch turn
            game.is_p1_turn = False
            action = input("Would you like to use your left hand (L), your right hand (R), or split (S)?").upper()
            while action not in {'L', 'R', 'S'}:
                action = input("Please choose either left (L), right (R), or split (S).").upper()
            
            if action in {'L', 'R'}:
                target = input("Would you like to attack your opponent's left hand (L) or right hand (R)?").upper()
                while target not in {'L', 'R'}:
                    target = input("Please choose either your opponent's left (L) or right (R)").upper()
                if action == 'L':
                    game.p2.add(target, game.p1.left.num_fingers)
                else:
                    #Action from Right hand
                    game.p2.add(target, game.p1.right.num_fingers)

            else:
                #Must be splitting
                newL = int(input("What new value would you like your left to be?"))
                newR = int(input("What new value would you like your right to be?"))
                while not game.p1.split(newL, newR):
                    newL = int(input("Incompatible values. Input an acceptable value for your new left "))
                    newR = int(input("And your new right "))
                
        else:
            #Switch turn
            game.is_p1_turn = True
    
    if game.winner() == 1:
        print("Congrats! You won!")
    elif game.winner() == -1:
        print("Sorry, you didn't win this time.")
    else:
        print("Error occurred.")