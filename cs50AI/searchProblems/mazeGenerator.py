import random

def generate_maze(width, height):
    maze = [["#" for _ in range(width)] for _ in range(height)]
    
    # Generate random start and finish positions
    start = (random.randint(1, width-2), random.randint(1, height-2))
    finish = (random.randint(1, width-2), random.randint(1, height-2))
    
    maze[start[1]][start[0]] = "A"
    maze[finish[1]][finish[0]] = "B"
    
    # Generate a clear path from A to B
    x, y = start
    while (x, y) != finish:
        nx, ny = random.choice([(x+1, y), (x-1, y), (x, y+1), (x, y-1)])
        if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == "#":
            maze[ny][nx] = " "
        x, y = nx, ny
    
    return maze

def save_maze_to_file(maze):
    with open("maze.txt", "w") as file:
        for row in maze:
            file.write(" ".join(row) + "\n")

def main():
    width = int(input("Enter width of the maze: "))
    height = int(input("Enter height of the maze: "))
    
    maze = generate_maze(width, height)
    save_maze_to_file(maze)
    print("Maze saved to 'maze.txt'")

if __name__ == "__main__":
    main()