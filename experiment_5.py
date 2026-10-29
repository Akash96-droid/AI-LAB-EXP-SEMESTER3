# Program to implement the minimax algorithm

def minimax(depth, nodeIndex, isMax, scores, height):
    # Terminating condition: leaf node is reached
    if depth == height:
        return scores[nodeIndex]
    
    if isMax:
        # Maximizer: choosing the maximum value between left and right children
        return max(
            minimax(depth + 1, nodeIndex * 2, False, scores, height),
            minimax(depth + 1, nodeIndex * 2 + 1, False, scores, height)
        )
    else:
        # Minimizer: choosing the minimum value between left and right children
        return min(
            minimax(depth + 1, nodeIndex * 2, True, scores, height),
            minimax(depth + 1, nodeIndex * 2 + 1, True, scores, height)
        )

# Main program
# Example leaf node values for a tree of height 3 (requires 2^3 = 8 values)
# e.g., 3, 5, 2, 9, 12, 5, 23, 23
scores = list(map(int, input("Enter leaf node values: ").split()))

# height = 3 means 2^3 = 8 leaf nodes
height = 3 

# Start the evaluation from the root node (depth 0, index 0, Maximizer's turn)
result = minimax(0, 0, True, scores, height)
print("The optimal value is :", result)
