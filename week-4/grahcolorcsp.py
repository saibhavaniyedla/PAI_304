import matplotlib.pyplot as plt

class GraphColoringCSP:
    def __init__(self, graph, colors):
        self.graph = graph
        self.nodes = list(graph.keys())
        self.colors = colors
        self.assignment = {}

    def is_safe(self, node, color):
        for neighbor in self.graph[node]:
            if neighbor in self.assignment and self.assignment[neighbor] == color:
                return False
        return True

    def backtrack(self, index=0):
        if index == len(self.nodes):
            return True

        node = self.nodes[index]

        for color in self.colors:
            if self.is_safe(node, color):
                self.assignment[node] = color
                if self.backtrack(index + 1):
                    return True
                del self.assignment[node]

        return False

    def solve(self):
        if self.backtrack():
            return self.assignment
        return None


# ----------------------------
# DEFINE GRAPH
# ----------------------------

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['A', 'B', 'C']
}

colors = ['red', 'green', 'blue']

csp = GraphColoringCSP(graph, colors)
solution = csp.solve()

# ----------------------------
# VISUALIZATION
# ----------------------------

if solution:
    print("Solution:", solution)

    # Fixed positions for nodes
    positions = {
        'A': (0, 1),
        'B': (-1, 0),
        'C': (0, -1),
        'D': (1, 0)
    }

    plt.figure()

    # Draw edges
    for node in graph:
        for neighbor in graph[node]:
            x = [positions[node][0], positions[neighbor][0]]
            y = [positions[node][1], positions[neighbor][1]]
            plt.plot(x, y, 'black')

    # Draw nodes
    for node, (x, y) in positions.items():
        plt.scatter(x, y, s=2000, c=solution[node])
        plt.text(x, y, node, fontsize=15,
                 ha='center', va='center', color='white')

    plt.title("Graph Coloring using CSP")
    plt.axis('off')
    plt.show()

else:
    print("No solution found.")
