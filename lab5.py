import math

def utility(sticks, is_max_turn):
    if sticks == 0:
        if is_max_turn:
            return -1
        else:
            return +1

def terminal(sticks):
    return sticks == 0

def successors(sticks):
    moves = []
    if sticks >= 1:
        moves.append(sticks - 1)
    if sticks >= 2:
        moves.append(sticks - 2)
    return moves

def minimax(sticks, is_max_turn):
    
    if terminal(sticks):
        return utility(sticks, is_max_turn)
    
    if is_max_turn:
        best = -math.inf
        for next_state in successors(sticks):
            val = minimax(next_state, False)
            best = max(best, val)
        return best
    
    else:
        best = math.inf
        for next_state in successors(sticks):
            val = minimax(next_state, True)
            best = min(best, val)
        return best

def best_move(sticks):
    best_val = -math.inf
    best_action = None
    
    for move in [1,2]:
        if sticks - move >= 0:
            val = minimax(sticks - move, False)
            if val > best_val:
                best_val = val
                best_action = move
    
    return best_action

sticks = 7
move = best_move(sticks)
print("Best move:", move)
