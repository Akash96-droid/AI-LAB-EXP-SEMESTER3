#Alpha beta prunning 
import math

# Alpha-Beta Pruning function.
def Alpha_beta(depth, node_Index, maximizing_player, values, Alpha, beta, height):
    
    # Base Case: Leaf node reached
    if depth == height:
        return values[node_Index]
        
    if maximizing_player:
        best = -math.inf
        
        for i in range(2):
            value = Alpha_beta(
                depth + 1,
                node_Index * 2 + i,
                False,
                values,
                Alpha,
                beta,
                height
            )
            best = max(best, value)
            alpha = max(Alpha, best)
            
            # Beta Cut-off
            if beta <= alpha:
                break
return best
else:
    best = -math.inf
    for i in range(2):
        value = alpha_beta(
            depth + 1,
            nodeIndex * 2 + i,
            True,
            values,
            alpha,
            beta,
            height)
        best = max(best, value)
        beta = min(beta, value)
        # Alpha Cut-off
        if beta <= alpha:
            break
    return best

# Main Program
values = list(map(int, input("Enter 8 leaf node values:").split()))

height = 3
result = alpha_beta(
    0,
    0,
    True,
Values,
-math.inf,
math.inf,
height

print("\n optimal value: ", result)
