import random


def generate_random_number():
    """Function to generate a random number between 1 and 9"""
    return random.randint(1, 9)

def generate_random_grid():
    """Function to generate a 3x3 grid of random numbers"""
    grid = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(generate_random_number())
        grid.append(row)
    return grid

def print_grid(grid):
    """Function to print the grid"""
    for row in grid:
        print(" ".join(map(str, row)))

def find_lowest_path(grid):
    rows = len(grid)
    cols = len(grid[0])

    """Initialize a DP table to store the lowest path sums"""
    dp = [[float('inf')] * cols for _ in range(rows)]
    dp[0][0] = grid[0][0]

    """Initialize a table to store the path"""
    path = [[""] * cols for _ in range(rows)]
    path[0][0] = str(grid[0][0])

    """Fill the DP table and path table"""
    for i in range(rows):
        for j in range(cols):
            if i > 0:
                if dp[i-1][j] + grid[i][j] < dp[i][j]:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                    path[i][j] = path[i-1][j] + " " + str(grid[i][j])
            if j > 0:
                if dp[i][j-1] + grid[i][j] < dp[i][j]:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                    path[i][j] = path[i][j-1] + " " + str(grid[i][j])

    """Return the lowest path sum and path"""
    return dp[rows-1][cols-1], path[rows-1][cols-1]

# Generate and print the random grid
random_grid = generate_random_grid()
print("Random 3x3 Grid:\n")
print_grid(random_grid)
print()

# Find and print the lowest path sum and path
lowest_path_sum, path_taken = find_lowest_path(random_grid)
print("Lowest numerical path sum:", lowest_path_sum)
print("Path taken:", path_taken)