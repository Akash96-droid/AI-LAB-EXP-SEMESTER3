# Travelling salesman problem 
from itertools import permutations

def travelling_salesman(graph, start):
    # Create a list of all city indices
    cities = list(range(len(graph)))
    # Remove the starting city from the list to permute only the remaining ones
    cities.remove(start)
    
    min_cost = float('inf')
    best_path = None
    
    # Generate all possible permutations of the remaining cities
    for perm in permutations(cities):
        current_cost = 0
        current_path = [start]
        k = start
        
        # Calculate the cost of the path through the permutation
        for city in perm:
            current_cost += graph[k][city]
            current_path.append(city)
            k = city
            
        # Add the cost to return to the starting city
        current_cost += graph[k][start]
        current_path.append(start)
        
        # Update the minimum cost and best path if a cheaper route is found
        if current_cost < min_cost:
            min_cost = current_cost
            best_path = current_path
            
    return best_path, min_cost
# Main program
if _name_ == "_main_":
    n = int(input("Enter the number of cities: "))
    print("Enter the cost matrix row by row (space-separated values): ")
    graph = []
    for i in range(n):
        row = list(map(int, input().split()))
        graph.append(row)
        
    start = int(input("Enter the starting city (0 to {}): ".format(n-1)))
    
    path, cost = traveling_salesman(graph, start)
    print("\nOptimal path: ", " -> ".join(map(str, path)))
    print("Minimum Cost: ", cost)
