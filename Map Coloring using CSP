def is_valid(node, color, assignment, graph):
    for neighbor in graph[node]:
        if assignment.get(neighbor) == color:
            return False
    return True

def backtrack(graph, colors, assignment):
    if len(assignment) == len(graph):
        return assignment

    unassigned = [node for node in graph if node not in assignment]
    node = unassigned[0]
    
    for color in colors:
        if is_valid(node, color, assignment, graph):
            assignment[node] = color
            result = backtrack(graph, colors, assignment)
            if result:
                return result
            assignment.pop(node)
    return None
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}
colors = ['Red', 'Green', 'Blue']
print(backtrack(graph, colors, {}))
