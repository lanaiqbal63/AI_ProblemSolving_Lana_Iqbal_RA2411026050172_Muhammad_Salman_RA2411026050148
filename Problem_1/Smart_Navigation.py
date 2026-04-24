from collections import deque

grid = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

rows = len(grid)
cols = len(grid[0])

start = (0, 0)
goal = (4, 4)

directions = [(-1,0), (1,0), (0,-1), (0,1)]

def bfs(grid, start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == goal:
            return path

        if (x, y) in visited:
            continue

        visited.add((x, y))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == 0 and (nx, ny) not in visited:
                    queue.append(((nx, ny), path + [(nx, ny)]))

    return None

path = bfs(grid, start, goal)

if path:
    print("Path found:")
    print(path)
else:
    print("No path found.")