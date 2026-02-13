# Goal state
goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]
def is_solvable(state):
    arr = []
    for row in state:
        for num in row:
            if num != 0:
                arr.append(num)
    inversions = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                inversions += 1
    return inversions % 2 == 0
def heuristic(state):
    h = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                h += 1
    return h
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
def get_children(state):
    x, y = find_blank(state)
    children = []
    moves = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
    for nx, ny in moves:
        if 0 <= nx < 3 and 0 <= ny < 3:
            new = [row[:] for row in state]
            new[x][y], new[nx][ny] = new[nx][ny], new[x][y]
            children.append(new)
    return children
def print_state(state):
    for row in state:
        print(*row)
    print("Heuristic =", heuristic(state))
    print("------------")
def astar(start):
    if not is_solvable(start):
        print("Puzzle is NOT Solvable ❌")
        return
    open_list = [(start, 0)]
    visited = []
    while open_list:
        open_list.sort(key=lambda x: heuristic(x[0]))
        current, moves_count = open_list.pop(0)
        print_state(current)
        if current == goal:
            print("Goal State Reached ✅")
            print("Total Moves =", moves_count)
            return
        visited.append(current)
        for child in get_children(current):
            if child not in visited:
                open_list.append((child, moves_count + 1))
print("Enter 8-puzzle values (use 0 for blank):")
start = []
for i in range(3):
    start.append(list(map(int, input().split())))
astar(start)
