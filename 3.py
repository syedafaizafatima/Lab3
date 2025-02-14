class Graph:
    def __init__(self, adjacency_list):
        """Initializes the graph with an adjacency list."""
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        """Returns the neighbors of a given node."""
        return self.adjacency_list[v]

    def h(self, n):
        """Heuristic function: estimates the cost from node n to the goal."""
        H = {
            'The': 4,
            'Cat': 3,
            'Dog': 3,
            'runs': 2,
            'fast': 1
        }
        return H[n]

    def a_star_algorithm(self, start_node, stop_node):
        """Implements the A* search algorithm to find the optimal path."""
        open_list = set([start_node])
        closed_list = set([])

        g = {}  # Cost from start node to all other nodes
        g[start_node] = 0

        parents = {}  # Keeps track of paths
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            # Find the node with the lowest f(n) = g(n) + h(n)
            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v

            if n == None:
                print("Path does not exist!")
                return None

            # If goal node is found, reconstruct and return the path
            if n == stop_node:
                path = []

                while parents[n] != n:
                    path.append(n)
                    n = parents[n]

                path.append(start_node)
                path.reverse()

                print('Path found:', ' -> '.join(path))
                print('Total Cost:', g[stop_node])
                return path

            # Explore all neighbors of the current node
            for (m, cost) in self.get_neighbors(n):
                # If the neighbor is not in both open and closed lists, add it to open list
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + cost

                # If the neighbor is already in open list, check if the new path is better
                else:
                    if g[m] > g[n] + cost:
                        g[m] = g[n] + cost
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)

        print("Path does not exist!")
        return None


# Define the graph using adjacency list
adjacency_list = {
    'The': [('Cat', 2), ('Dog', 3)],
    'Cat': [('runs', 1)],
    'Dog': [('runs', 2)],
    'runs': [('fast', 2)],
    'fast': []
}

graph1 = Graph(adjacency_list)
graph1.a_star_algorithm('The', 'fast')
