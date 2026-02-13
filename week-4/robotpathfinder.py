def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
def get_lowest_f(open_list, f_score):
    lowest = open_list[0]
    for node in open_list:
        if f_score[node] < f_score[lowest]:
            lowest = node
    return lowest
def astar(matrix, start, end):
    rows = len(matrix)
    cols = len(matrix[0])
    open_list = [start]
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}
    while open_list:
        current = get_lowest_f(open_list, f_score)
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, g_score[end]
        open_list.remove(current)
        x, y = current
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                neighbor = (nx, ny)
                tentative_g = g_score[current] + matrix[nx][ny]

                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + heuristic(neighbor, end)

                    if neighbor not in open_list:
                        open_list.append(neighbor)
    return None, None
r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))
matrix = []
print("Enter the matrix values row-wise (space separated):")
for _ in range(r):
    row = list(map(int, input().split()))
    matrix.append(row)
start = (0, 0)
end = (r-1, c-1)
path, cost = astar(matrix, start, end)
if path:
    for x, y in path:
        matrix[x][y] = '*'
    matrix[start[0]][start[1]] = 'S'
    matrix[end[0]][end[1]] = 'E'

    print("\nPath in Matrix:")
    for row in matrix:
        print(" ".join(map(str, row)))
    print("\nTotal cost:", cost)
else:
    print("No path found!")
