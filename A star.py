from queue import PriorityQueue

# Grid size
ROWS = 5
COLS = 5

# Heuristic Function (Manhattan Distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* Algorithm
def astar(grid, start, goal):

    pq = PriorityQueue()
    pq.put((0, start))

    came_from = {}
    cost_so_far = {}

    came_from[start] = None
    cost_so_far[start] = 0

    while not pq.empty():

        current = pq.get()[1]

        if current == goal:
            break

        neighbors = [
            (current[0] + 1, current[1]),
            (current[0] - 1, current[1]),
            (current[0], current[1] + 1),
            (current[0], current[1] - 1)
        ]

        for next in neighbors:

            x, y = next

            if 0 <= x < ROWS and 0 <= y < COLS and grid[x][y] == 0:

                new_cost = cost_so_far[current] + 1

                if next not in cost_so_far or new_cost < cost_so_far[next]:

                    cost_so_far[next] = new_cost

                    priority = new_cost + heuristic(goal, next)

                    pq.put((priority, next))

                    came_from[next] = current

    # Reconstruct Path
    path = []
    current = goal

    while current != start:
        path.append(current)
        current = came_from[current]

    path.append(start)
    path.reverse()

    return path

# 0 = Free Cell
# 1 = Obstacle
grid = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

path = astar(grid, start, goal)

print("Shortest Path:")
print(path)