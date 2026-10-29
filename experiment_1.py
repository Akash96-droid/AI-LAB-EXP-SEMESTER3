# to implement BFS using python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    print("BFS Traversal: ", end="")
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")
        
        # Traverse neighbors of the current vertex
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    print() # Newline after traversal finishes

# --- Graph Input Logic ---
graph = {}
n = int(input("Enter the number of vertices: "))

for i in range(n):
    vertex = input(f"Enter vertex {i+1}: ").strip()
    
    # Take space-separated adjacent vertices (e.g., "B C D")
    adj_input = input(f"Enter adjacent vertices of {vertex} (space-separated, e.g., B C): ")
    
    # Process neighbors: split by spaces if the input is not empty
    neighbors = [m.strip() for m in adj_input.split() if m.strip()]
    
    graph[vertex] = neighbors

# --- Execution ---
if graph:
    # Pick the first entered vertex as the starting point automatically
    start_vertex = list(graph.keys())[0] 
    bfs(graph, start_vertex)
graph[vertex] = neighbours
Start = input("Enter the starting vertex: ")
print("\n Graph: ", graph)
bfs(graph, Start)
