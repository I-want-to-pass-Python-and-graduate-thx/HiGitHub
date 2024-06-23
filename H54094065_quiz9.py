import random

def generate_path(maze, N, M):
    # Generates a random path from (0,0) to (N-1,M-1)
    path = [(0, 0)]
    current = (0, 0)
    while current != (N-1, M-1):
        # Randomly decide to move right or down, ensuring we don't go out of bounds
        if current[0] < N-1 and (current[1] == M-1 or random.choice([True, False])):
            current = (current[0] + 1, current[1])
        else:
            current = (current[0], current[1] + 1)
        path.append(current)
    # Mark the path in the maze
    for cell in path:
        maze[cell] = 2
    return maze

def add_obstacles(maze, min_obstacles, N, M):
    # Add at least min_obstacles randomly to the maze
    empty_cells = [(i, j) for i in range(N) for j in range(M) if maze[(i, j)] == 0]
    for _ in range(min_obstacles):
        try:
            cell = random.choice(empty_cells)
            maze[cell] = 1
            empty_cells.remove(cell)
        except IndexError:
            print("Error: Could not place obstacle. Not enough empty cells.")
            break

def set_obstacle(maze, N, M):
    # Allow user to manually set an obstacle in the maze
    try:
        x, y = map(int, input("Enter the coordinates to set an obstacle (x y): ").split())
        if maze[(x, y)] == 2:
            print("Error: Cannot place an obstacle on the path.")
        else:
            maze[(x, y)] = 1
    except KeyError:
        print("Error: Coordinates out of bounds.")
    except ValueError:
        print("Error: Invalid input. Please enter integer coordinates.")

def remove_obstacle(maze, N, M):
    # Allow user to manually remove an obstacle from the maze
    try:
        x, y = map(int, input("Enter the coordinates to remove an obstacle (x y): ").split())
        if maze[(x, y)] == 1:
            maze[(x, y)] = 0
        else:
            print("Error: No obstacle at the given coordinates.")
    except KeyError:
        print("Error: Coordinates out of bounds.")
    except ValueError:
        print("Error: Invalid input. Please enter integer coordinates.")

def print_maze(maze, N, M):
    # Print the current state of the maze
    for i in range(N):
        row = ''
        for j in range(M):
            if maze[(i, j)] == 0:
                row += '   '  # Empty cell
            elif maze[(i, j)] == 1:
                row += ' X '  # Obstacle
            elif maze[(i, j)] == 2:
                row += ' O '  # Path
            row += '|'
        print(row)
        print('+---' * M + '+')

def main():
    # Main function to drive the program
    file_name = input("Enter file name: ")
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
        # Determine maze dimensions
        N = len(lines) // 2
        M = len(lines[0].split('|')) - 1
        # Initialize maze with all empty cells
        maze = {(i, j): 0 for i in range(N) for j in range(M)}
    except IOError:
        print("IOError occurred in main function. File not found. Please enter a valid file name.")
        return
    except NameError:
        print("Error: Invalid file format.")
        return

    print_maze(maze, N, M)
    help_message = "Enter the column followed by the row (ex: a5). To add or remove a flag, add 'f' to the cell (ex: a5f). Type 'help' to show this message again."

    while True:
        try:
            min_obstacles = int(input("Enter the minimum number of obstacles (0-55): "))
            if 0 <= min_obstacles <= 55:
                break
            else:
                print("Invalid number of obstacles. Please enter a number between 0 and 55.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    maze = generate_path(maze, N, M)
    add_obstacles(maze, min_obstacles, N, M)
    print_maze(maze, N, M)

    print(help_message)

    while True:
        print("\nOptions:")
        print("1. Set obstacle")
        print("2. Remove obstacle")
        print("3. Exit")
        option = input("Enter your option: ")
        
        if option == '1':
            set_obstacle(maze, N, M)
        elif option == '2':
            remove_obstacle(maze, N, M)
        elif option == '3':
            break
        else:
            print("Invalid option. Please choose a valid option.")
        
        print_maze(maze, N, M)

if __name__ == "__main__":
    main()
