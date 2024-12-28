from queue import PriorityQueue

def a_star(graph, start, goal, heuristic):
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    while not open_set.empty():
        _, current = open_set.get()
        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor, weight in graph[current].items():
            tentative_g = g_score[current] + weight
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic[neighbor]
                open_set.put((f_score, neighbor))

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 1},
    'C': {'D': 1},
    'D': {}
}
heuristic = {'A': 3, 'B': 2, 'C': 1, 'D': 0}
print(a_star(graph, 'A', 'D', heuristic))
