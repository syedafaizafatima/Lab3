import time
from collections import deque

# Convert state string to a tuple of tuples (immutable representation)
def state_to_tuple(state):
    return tuple(tuple(state[i:i+3]) for i in range(0, 9, 3))


def get_moves(matrix):
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == '0':
                x, y = i, j
                break
    
   
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    moves = []
    
    for dx, dy in directions:
        neighbour_x, neighbour_y = x + dx, y + dy
        
        # Check boundaries
        if 0 <= neighbour_x < 3 and 0 <= neighbour_y < 3:
            # Swap blank space with the adjacent tile
            new_matrix = [list(row) for row in matrix]
            new_matrix[x][y], new_matrix[neighbour_x][neighbour_y] = new_matrix[neighbour_x][neighbour_y], new_matrix[x][y]
            moves.append(tuple(tuple(row) for row in new_matrix))
    
    return moves


def dfs(start_state, goal_state, max_depth=30):
    stack = [(start_state, [])]  # Stack stores (current_state, path_taken)
    visited = set()              # Set of visited states
    
    while stack:
        current_state, path = stack.pop()
        
        
        if current_state == goal_state:
            return path + [current_state]
        

        visited.add(current_state)
        
        # Limit depth to avoid infinite loops
        if len(path) >= max_depth:
            continue
    
        for move in get_moves(current_state):  
            if move not in visited and move not in path:  # Avoid revisiting in current path
                stack.append((move, path + [current_state]))
    
    return None 




def main():
    start_state = input("Enter start State (e.g., 120345678): ")
    goal_state = input("Enter goal State (e.g., 012345678): ")
    
    
  
    
    # Convert states to tuple format
    start_tuple = state_to_tuple(start_state)
    goal_tuple = state_to_tuple(goal_state)
    
    print("-----------------")
    print("DFS Algorithm")
    print("-----------------")
    
    start_time = time.time()
    solution_path = dfs(start_tuple, goal_tuple)
    end_time = time.time()
    
    if solution_path:
        print("Time taken:", end_time - start_time, "seconds")
        print("Path Cost:", len(solution_path) - 1)
        print("No of Nodes Visited:", len(solution_path))
        
        for state in solution_path:
            for row in state:
                print(' '.join(row))
            print("-----")
    else:
        print("No solution found or depth limit reached.")

if __name__ == "__main__":
    main()
