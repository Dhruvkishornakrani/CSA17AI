def solve_queens(n, board=[], solutions=[]):
    if len(board) == n:
        solutions.append(board)
        return
    for col in range(n):
        if all(col != c and abs(len(board) - r) != abs(col - c) for r, c in enumerate(board)):
            solve_queens(n, board + [col], solutions)
    return solutions
n = 8
solutions = solve_queens(n)
for solution in solutions:
    for row in solution:
        print("." * row + "Q" + "." * (n - row - 1))
    print()
