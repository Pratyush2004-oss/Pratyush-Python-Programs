def ao_star_search(graph, start, goal, heuristic):
    solved = set()
    g = {node: float('inf') for node in graph}
    h = heuristic.copy()
    g[start] = 0
    
    while goal not in solved:
        # Select an unsolved node with minimal f = g + h
        unsolved = [node for node in graph if node not in solved]
        if not unsolved:
            break
            
        current = min(unsolved, key=lambda node: g[node] + h[node])
        
        if current == goal:
            solved.add(current)
            break
            
        # Expand the current node
        for neighbor, cost in graph[current].items():
            if g[current] + cost < g[neighbor]:
                g[neighbor] = g[current] + cost
                
        # Mark current as solved if all children are solved
        if all(neighbor in solved for neighbor in graph[current]):
            solved.add(current)
    
    # Reconstruct path
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = min(graph[current].items(), key=lambda x: g[x[0]] + x[1])[0]
    path.append(start)
    path.reverse()
    
    return path, g[goal]

# Example usage
graph = {
    'A': {'B': 2, 'D': 3},
    'B': {'A': 2, 'C': 1, 'D': 4},
    'C': {'B': 1, 'D': 2, 'E': 3},
    'D': {'A': 3, 'B': 4, 'C': 2, 'E': 2},
    'E': {'C': 3, 'D': 2}
}
heuristic = {'A': 6, 'B': 4, 'C': 3, 'D': 2, 'E': 0}

path, cost = ao_star_search(graph, 'A', 'E', heuristic)
print("AO* Path:", path)
print("Total Cost:", cost)