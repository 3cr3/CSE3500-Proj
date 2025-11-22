from chopsticks import GameState, Player, Hand
from minimax import minimax
import sys
sys.setrecursionlimit(1000000)

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
            game = minimax(game)
    
    if game.winner() == -1:
        print("Congrats! You won!")
    elif game.winner() == 1:
        print("Sorry, you didn't win this time.")
    else:
        print("Error occurred.")