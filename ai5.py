from collections import deque

def is_valid(state):
    m1, c1, m2, c2, boat = state
    if (m1 < c1 and m1 > 0) or (m2 < c2 and m2 > 0):
        return False
    if m1 < 0 or c1 < 0 or m2 < 0 or c2 < 0:
        return False
    return True

def missionaries_and_cannibals():
    start = (3, 3, 0, 0, 1)  
    goal = (0, 0, 3, 3, 0)   
    queue = deque([(start, [])])  
    visited = set()

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path + [state]

        if state in visited:
            continue
        visited.add(state)

        m1, c1, m2, c2, boat = state
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]  

        for m, c in moves:
            if boat:  
                new_state = (m1 - m, c1 - c, m2 + m, c2 + c, 0)
            else:  
                new_state = (m1 + m, c1 + c, m2 - m, c2 - c, 1)

            if is_valid(new_state):
                queue.append((new_state, path + [state]))

    return "No solution"

solution = missionaries_and_cannibals()
for step in solution:
    print(step)
