from chopsticks import GameState, Player, Hand


def generate_moves(state):
    myL, myR, oppL, oppR = state.p2.left.num_fingers, state.p2.right.num_fingers, state.p1.left.num_fingers, state.p1.right.num_fingers


    new_states = []

    #attacking moves
    for myHand in [myL, myR]:
        if myHand != 0:
            for oppHand in ['L', 'R']:
                newState = state.copy()
                if oppHand == 'L' and oppL > 0:
                    newState.p1.left.add(myHand)
                elif oppHand == 'R' and oppR > 0:
                    newState.p1.right.add(myHand)
                new_states.append(newState)
        
    #splitting moves
    total = myL + myR
    for a in range(0, 5):
        b = total - a
        if 0 <= b <= 4 and b != myL and b!= myR:
            newState = state.copy()
            newState.p2.split(a, b)
            new_states.append(newState)
    
    return new_states


def minimax(state):
    if state.is_terminal():
        return state.winner()
    newState = state.copy()
    return newState

def getbestmove():

def apply_move():
