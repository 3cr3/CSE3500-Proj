from chopsticks import GameState, Player, Hand
from math import inf
import sys
sys.setrecursionlimit(1000000)

def generate_moves(state, player):
    myL, myR, oppL, oppR = (
        state.p2.left.num_fingers, state.p2.right.num_fingers, 
        state.p1.left.num_fingers, state.p1.right.num_fingers
    ) if player == 0 else (
        state.p1.left.num_fingers, state.p1.right.num_fingers, 
        state.p2.left.num_fingers, state.p2.right.num_fingers
    )


    new_states = []

    #attacking moves
    for myHand in [myL, myR]:
        if myHand != 0:
            for oppHand in ['L', 'R']:
                newState = state.copy()
                if oppHand == 'L' and oppL > 0:
                    if player == 0:
                        newState.p1.left.add(myHand)
                    else:
                        newState.p2.left.add(myHand)
                elif oppHand == 'R' and oppR > 0:
                    if player == 0:
                        newState.p1.right.add(myHand)
                    else:
                        newState.p2.right.add(myHand)
                if not newState.equals(state): new_states.append(newState)
        
    #splitting moves
    total = myL + myR
    for a in range(0, 5):
        b = total - a
        if 0 <= b <= 4 and sorted((a,b)) != sorted((myL,myR)):
            newState = state.copy()
            if player == 0:
                if (newState.p2.split(a, b)): new_states.append(newState)
            else:
                if (newState.p1.split(a,b)): new_states.append(newState)
            # new_states.append(newState)
    
    return new_states


def minimax(state, is_maximizing, depth, max_depth):
    if state.is_terminal():
        return state.winner()*10000, state
    if depth >= max_depth:
        return evaluate(state, 0), state if is_maximizing else evaluate(state, 1), state
    if is_maximizing:
        moves = generate_moves(state, player=0)
        if not moves:
            return evaluate(state, 0), state
        best = -inf
        best_m = state.copy()
        for move in moves:
            val = minimax(move, False, depth+1, max_depth)[0]
            if val > best:
                best = val
                if not move.equals(state):
                    best_m = move
    else:
        moves = generate_moves(state, player=1)
        if not moves:
            return evaluate(state, 1), state
        best = inf
        for move in moves:
            val = minimax(move, True, depth+1, max_depth)[0]
            if val < best:
                best = val
                if not move.equals(state):
                    best_m = move
            


    return (best, best_m)


# ~~~~~DISCLAIMER~~~~~
# evaluate function was created using AI, because the state evaluation function is not
# a part of understanding minimax, and it is specific to each game. 
def evaluate(state, player):
    """
    Returns a score estimating how good the state is for `player`.
    Higher = better for player.
    """

    # unpack
    pL, pR, oL, oR = (
        state.p2.left.num_fingers, state.p2.right.num_fingers, 
        state.p1.left.num_fingers, state.p1.right.num_fingers
    ) if player == 0 else (
        state.p1.left.num_fingers, state.p1.right.num_fingers, 
        state.p2.left.num_fingers, state.p2.right.num_fingers
    )
    
    score = 0

    # ---------------------------
    # 1. Check for terminal wins
    # ---------------------------
    if oL == 0 and oR == 0:
        return 10_000      # winning state
    if pL == 0 and pR == 0:
        return -10_000     # losing state

    # ---------------------------
    # 2. Dead hand advantage
    # ---------------------------
    p_dead = (pL == 0) + (pR == 0)
    o_dead = (oL == 0) + (oR == 0)
    score += 800 * (o_dead - p_dead)

    # ---------------------------
    # 3. Mobility / number of legal moves
    # ---------------------------
    # (States where you have few/no good moves are bad)
    score += 5 * (
        (pL > 0) + (pR > 0)
        - (oL > 0) - (oR > 0)
    )

    # ---------------------------
    # 4. Threat potential
    #    If a hand can kill an enemy hand next turn (x + my >= 5)
    # ---------------------------
    for my in [pL, pR]:
        if my == 0: continue
        for opp in [oL, oR]:
            if opp == 0: continue
            if my + opp >= 5:
                score += 50     # you threaten a kill
            if opp + my >= 5:
                score -= 50     # opponent threatens a kill

    # ---------------------------
    # 5. Value hands based on their modular position
    #    (4 is dangerous, 1–3 are flexible)
    # ---------------------------
    hand_value = [0, 10, 15, 25, -10]  # custom weights
    score += hand_value[pL] + hand_value[pR]
    score -= hand_value[oL] + hand_value[oR]

    # ---------------------------
    # 6. Prefer asymmetry in your hands
    #    {2,3} gives more options than {2,2}
    # ---------------------------
    if pL != pR:
        score += 8
    if oL != oR:
        score -= 8

    return score
# def getbestmove():

# def apply_move():
