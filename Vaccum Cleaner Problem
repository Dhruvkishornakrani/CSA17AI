def vacuum_cleaner(room, start):
    x, y = start
    print("Initial Room:")
    for row in room:
        print(row)

    steps = 0
    for i in range(len(room)):
        for j in range(len(room[i])):
            if room[x][y] == 1: 
                room[x][y] = 0
                print(f"Cleaned cell ({x}, {y})")
            steps += 1
            y += 1
            if y == len(room[i]):
                x += 1
                y = 0

    print("\nFinal Room:")
    for row in room:
        print(row)
    print(f"\nTotal steps taken: {steps}")

room = [
    [1, 0, 1],
    [1, 1, 0],
    [0, 1, 1]
]
start = (0, 0)
vacuum_cleaner(room, start)
