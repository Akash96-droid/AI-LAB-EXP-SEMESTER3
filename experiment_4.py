# A* algorithm for searching
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 6)],
    'C': [('F', 5)],
    'D': [('H', 2)],
    'E': [('H', 1)],
    'F': [('H', 2)],
    'H': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 2,
    'H': 0
}

def astar(start, goal):
open_list = [(Start, 0)]
came_from = {}
g_cost = {Start : 0}

while open_list:
    # Select node with minimum f = g+h
    Current = min(open_list, key = lambda x : x[1] + heuristic(x[0]))
    open_list.remove(Current)
    Current_node = Current[0]
    
    if Current_node == goal:
        Path = [goal]
        while Current_node in came_from:
            Current_node = came_from[Current_node]
            Path.append(Current_node)
        Path.reverse()
        return Path, g_cost[goal]
        
    for neighbor, Cost in graph[Current_node]:
        new_cost = g_cost[Current_node] + Cost
        if neighbor not in g_cost or new_cost < g_cost[neighbor]:
            came_from[neighbor] = Current_node
            g_cost[neighbor] = new_cost
            open_list.append((neighbor, new_cost))
return Name, float('inf')

# main program
Start = input("Enter the start node: ")
goal = input("Enter the goal node: ")
Path, Cost = astar(start, goal)

if Path:
    print("The Shortest Path: ", " -> ".join(path))
    print("Total Cost: ", Cost)
else:
    print("Path not found.")
