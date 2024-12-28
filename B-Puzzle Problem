import heapq

class Puzzle:
    def __init__(self, state, parent, move, depth, cost):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

def heuristic(state, goal):
    """Calculate Manhattan distance."""
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_x, goal_y = divmod(goal.index(state[i][j]), 3)
                distance += abs(goal_x - i) + abs(goal_y - j)
    return distance

def get_neighbors(state):
    """Generate neighbor states by moving the blank space (0)."""
    neighbors = []
    x, y = next((i, j) for i in range(3) for j in range(3) if state[i][j] == 0)
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append((new_state, (nx, ny)))
    return neighbors

def a_star_search(start, goal):
    """Solve the 8-puzzle using A* search."""
    goal_flat = [num for row in goal for num in row]
    visited = set()
    pq = []
    initial_cost = heuristic(start, goal_flat)
    root = Puzzle(start, None, None, 0, initial_cost)
    heapq.heappush(pq, root)
    
    while pq:
        current = heapq.heappop(pq)
        visited.add(tuple(tuple(row) for row in current.state))
        
        if current.state == goal:
            path = []
            while current.parent:
                path.append(current.move)
                current = current.parent
            return path[::-1]
        
        for neighbor, _ in get_neighbors(current.state):
            if tuple(tuple(row) for row in neighbor) not in visited:
                g_cost = current.depth + 1
                h_cost = heuristic(neighbor, goal_flat)
                total_cost = g_cost + h_cost
                heapq.heappush(pq, Puzzle(neighbor, current, neighbor, g_cost, total_cost))
    return None

def print_solution(path, start):
    """Print the solution steps."""
    state = start
    print("Initial State:")
    for row in state:
        print(row)
    for step, move in enumerate(path, start=1):
        print(f"\nStep {step}:")
        for row in move:
            print(row)

# Input
start = [[1, 2, 3], [5, 0, 6], [4, 7, 8]]
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Solve the problem
solution = a_star_search(start, goal)
if solution:
    print_solution(solution, start)
else:
    print("No solution found.")
