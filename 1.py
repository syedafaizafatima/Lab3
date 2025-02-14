from collections import deque

# Define movements: up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Function to find position of a target value in matrix
def find_position(matrix, target):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == target:
                return i, j
    return None

# BFS Algorithm to find the shortest path and mark it
def bfs(matrix):
    start = find_position(matrix, -1)  # Find Ali's starting position
    goal = find_position(matrix, 1)    # Find the home position
    
    if not start or not goal:
        print("Starting point or home not found.")
        return
    
    queue = deque([(start, [])])  # Queue stores (current position, path taken)
    visited = set([start])        # Set of visited nodes
    
    while queue:
        (x, y), path = queue.popleft()
        
        # Check if home is reached
        if (x, y) == goal:
            print("Ali reached home!")
            
            # Mark the path in the matrix with '*'
            for step in path:
                px, py = step
                if matrix[px][py] == 0:  # Don't overwrite start or goal
                    matrix[px][py] = '*'
            
            # Print the final matrix
            print("Path Marked in Matrix:")
            for row in matrix:
                print(' '.join(str(cell) for cell in row))
            return
        
        # Explore neighbors
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            
            # Check boundaries and if the node is not visited
            if (0 <= new_x < len(matrix) and 0 <= new_y < len(matrix[0]) and 
                (new_x, new_y) not in visited):
                
                visited.add((new_x, new_y))
                queue.append(((new_x, new_y), path + [(x, y)]))
    
    print("No path to home found.")

# Sample Matrix
matrix = [
    [0, 0, 0, -1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0]
]

bfs(matrix)
