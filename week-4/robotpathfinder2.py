def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(cost_matrix, start, goal):
    rows, cols = len(cost_matrix), len(cost_matrix[0])
    open_list = [start]
    
    g_score = {start: 0}
    came_from = {}
    
    while open_list:
        # find node with minimum f_score
        current = min(open_list, key=lambda node: g_score[node] + heuristic(node, goal))
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        open_list.remove(current)
        
        x, y = current
        neighbors = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
        
        for nx, ny in neighbors:
            if 0 <= nx < rows and 0 <= ny < cols:
                
                if cost_matrix[nx][ny] == 0:   # obstacle
                    continue
                
                temp_g = g_score[current] + cost_matrix[nx][ny]
                
                if (nx,ny) not in g_score or temp_g < g_score[(nx,ny)]:
                    g_score[(nx,ny)] = temp_g
                    came_from[(nx,ny)] = current
                    
                    if (nx,ny) not in open_list:
                        open_list.append((nx,ny))
    
    return None


# -------- Runtime Input --------

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

cost_matrix = []

print("Enter the cost matrix row by row (use 0 for obstacles):")
for i in range(rows):
    row = list(map(int, input().split()))
    cost_matrix.append(row)

start_x = int(input("Enter start row: "))
start_y = int(input("Enter start column: "))

goal_x = int(input("Enter goal row: "))
goal_y = int(input("Enter goal column: "))

start = (start_x, start_y)
goal = (goal_x, goal_y)

path = astar(cost_matrix, start, goal)

# -------- Output Grid --------

if path:
    print("\nGrid with Shortest Path:\n")
    for i in range(rows):
        for j in range(cols):
            if (i,j) in path:
                print("*", end="  ")
            else:
                print(cost_matrix[i][j], end="  ")
        print()
else:
    print("No path found.")
