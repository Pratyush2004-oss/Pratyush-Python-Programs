import heapq

def a_star_search(graph, start, goal, heuristic):
    open_set = []
    heapq.heappush(open_set, (0 + heuristic[start], start))
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic[start]
    
    while open_set:
        current = heapq.heappop(open_set)[1]
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, f_score[goal]
        
        for neighbor, cost in graph[current].items():
            tentative_g_score = g_score[current] + cost
            
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic[neighbor]
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return None, float('inf')

# Example usage
graph = {
    'A': {'B': 2, 'D': 3},
    'B': {'A': 2, 'C': 1, 'D': 4},
    'C': {'B': 1, 'D': 2, 'E': 3},
    'D': {'A': 3, 'B': 4, 'C': 2, 'E': 2},
    'E': {'C': 3, 'D': 2}
}

heuristic = {'A': 6, 'B': 4, 'C': 3, 'D': 2, 'E': 0}

path, cost = a_star_search(graph, 'A', 'E', heuristic)
print("A* Path:", path)
print("Total Cost:", cost)