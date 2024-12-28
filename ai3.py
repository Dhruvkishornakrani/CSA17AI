from collections import deque

def water_jug_problem(capacity1, capacity2, target):
    visited = set()
    queue = deque([(0, 0)]) 

    while queue:
        jug1, jug2 = queue.popleft()

        if jug1 == target or jug2 == target:
            return f"Solved: Jug1 = {jug1}, Jug2 = {jug2}"

        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))

        queue.extend([
            (capacity1, jug2),  
            (jug1, capacity2),  
            (0, jug2),          
            (jug1, 0),          
            (max(0, jug1 + jug2 - capacity2), min(capacity2, jug1 + jug2)), 
            (min(capacity1, jug1 + jug2), max(0, jug1 + jug2 - capacity1))  
        ])

    return "No solution"

capacity1 = 4  
capacity2 = 3  
target = 2     
print(water_jug_problem(capacity1, capacity2, target))
