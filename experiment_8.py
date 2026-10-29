# water jug problem 
from collections import deque

def water_jug(capacity1, capacity2, target):
    if target > capacity1 + capacity2:
        return None
        
    visited = set()
    queue = deque()
    queue.append((0, 0, []))
    
    while queue:
        jug1, jug2, path = queue.popleft()
        
        if (jug1, jug2) in visited:
            continue
            
        visited.add((jug1, jug2))
        path = path + [(jug1, jug2)]
        
        if jug1 == target or jug2 == target:
            return path
            
        p1_to_p2 = min(jug1, capacity2 - jug2)
        p2_to_p1 = min(jug2, capacity1 - jug1)
        
        next_states = [
            (capacity1, jug2),
            (jug1, capacity2),
            (0, jug2),
            (jug1, 0),
            (jug1 - p1_to_p2, jug2 + p1_to_p2),
            (jug1 + p2_to_p1, jug2 - p2_to_p1)
        ]
        
        for state in next_states:
if nxt_state not in visited:
            queue.append((state[0], state[1], path))
    return None

#Main Program:
jug1 = int(input("Enter the capacity of jug 1: "))
jug2 = int(input("Enter the capacity of jug 2: "))
target = int(input("Enter target amount: "))
solution = water_jug(jug1, jug2, target)
if solution:
    print("\nSteps to reach the target:")
    for step in solution:
        print(step)
else:
    print("No solution exists.")
