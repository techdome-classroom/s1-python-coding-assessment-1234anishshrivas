#dispatch-1
def num_islands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or
                grid[r][c] == 'W' or (r, c) in visited):
            return
        visited.add((r, c))
        dfs(r + 1, c)  # Down
        dfs(r - 1, c)  # Up
        dfs(r, c + 1)  # Right
        dfs(r, c - 1)  # Left

    island_count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'L' and (r, c) not in visited:
                island_count += 1
                dfs(r, c)

    return island_count


print(num_islands(map_example)) 

 # Output: 1

#dispatch-2

def num_islands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or
                grid[r][c] == 'W' or (r, c) in visited):
            return
        visited.add((r, c))
        dfs(r + 1, c)  # Down
        dfs(r - 1, c)  # Up
        dfs(r, c + 1)  # Right
        dfs(r, c - 1)  # Left

    island_count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'L' and (r, c) not in visited:
                island_count += 1
                dfs(r, c)

    return island_count

# Example usage
print(num_islands(map_example))  # Output: 3
