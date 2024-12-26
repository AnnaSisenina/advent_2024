import os.path

# Load data from the file
filename = "input6.txt"
current_directory = os.path.dirname(os.path.abspath(__file__))
path = current_directory

try:
    with open(os.path.join(path, filename), "r") as file:
        data = [list(line.strip()) for line in file.read().splitlines()]
except Exception as e:
    print("Failed to create file for int:", e)

# Set for storing obstacles
hashes = set()  # Obstacles
start_pos = None  # Guard's position
directions = ['up', 'right', 'down', 'left']  # Directions
dir_moves = {  # Translate directions into coordinates
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

# Find the starting position and add obstacles
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == '#':
            hashes.add((i, j))
        elif data[i][j] == '^':
            start_pos = (i, j)
            start_direction = 'up'

# Function to check for guard looping
def check_loop(new_obstacle):
    visited = set()
    i, j = start_pos
    direction_index = directions.index(start_direction)

    while True:
        # Remember the current position
        if (i, j, direction_index) in visited:
            return True  # Looping
        visited.add((i, j, direction_index))

        # Check if the guard can move forward
        ni, nj = i + dir_moves[directions[direction_index]][0], j + dir_moves[directions[direction_index]][1]

        # If there is an obstacle ahead
        while (ni, nj) in hashes:
            # Turn right
            direction_index = (direction_index + 1) % 4
            ni, nj = i + dir_moves[directions[direction_index]][0], j + dir_moves[directions[direction_index]][1]

        # If the guard goes out of bounds, end the check
        if ni < 0 or ni >= len(data) or nj < 0 or nj >= len(data[0]):
            return False  

        # Update the position
        i, j = ni, nj

# Count possible positions for the new obstacle
possible_positions = 0
obstacles = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == '.':
            # Temporarily add an obstacle
            hashes.add((i, j))
            if check_loop((i, j)):
                possible_positions += 1
                obstacles.append([i, j])
            hashes.remove((i, j))  # Remove the obstacle after checking

print(hashes)
print(possible_positions)