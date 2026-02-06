def next_states(state, capacity):
    states = []
    for i in range(3):
        for j in range(3):
            if i != j:
                temp = list(state)
                pour = min(temp[i], capacity[j] - temp[j])
                if pour > 0:
                    temp[i] -= pour
                    temp[j] += pour
                    states.append(tuple(temp))
    return states
#BFS
def bfs(capacity, start, target):
    queue = [start]
    visited = [start]
    parent = {start: None}
    while queue:
        current = queue.pop(0)
        if target in current:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for s in next_states(current, capacity):
            if s not in visited:
                visited.append(s)
                parent[s] = current
                queue.append(s)
    return None
#DFS
def dfs(state, capacity, target, visited, path):
    visited.append(state)
    path.append(state)
    if target in state:
        return True
    for s in next_states(state, capacity):
        if s not in visited:
            if dfs(s, capacity, target, visited, path):
                return True
    path.pop()
    return False
capacity = tuple(map(int, input("Enter capacities (A B C): ").split()))
start = tuple(map(int, input("Enter start state (A B C): ").split()))
target = int(input("Enter target amount: "))
choice = input("Choose search (bfs / dfs): ").lower()
if choice == "bfs":
    result = bfs(capacity, start, target)
    print("\nBFS Solution:")
    for step in result:
        print(step)
elif choice == "dfs":
    path = []
    dfs(start, capacity, target, [], path)
    print("\nDFS Solution:")
    for step in path:
        print(step)
else:
    print("Invalid choice")
