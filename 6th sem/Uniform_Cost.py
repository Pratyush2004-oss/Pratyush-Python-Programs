import heapq

def uniform_cost_search(graph, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    cost_so_far = {node: float('inf') for node in graph}
    cost_so_far[start] = 0
    
    while open_set:
        current_cost, current = heapq.heappop(open_set)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, cost_so_far[goal]
        
        for neighbor, cost in graph[current].items():
            new_cost = current_cost + cost
            if new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                came_from[neighbor] = current
                heapq.heappush(open_set, (new_cost, neighbor))
    
    return None, float('inf')

# Example usage
graph = {
    'A': {'B': 2, 'D': 3},
    'B': {'A': 2, 'C': 1, 'D': 4},
    'C': {'B': 1, 'D': 2, 'E': 3},
    'D': {'A': 3, 'B': 4, 'C': 2, 'E': 2},
    'E': {'C': 3, 'D': 2}
}

path, cost = uniform_cost_search(graph, 'A', 'E')
print("Uniform Cost Path:", path)
print("Total Cost:", cost)