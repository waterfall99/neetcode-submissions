class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        island_count = 0
        
        def explore_island(r, c):
            if int(r) < 0 or int(r) >= len(grid) or int(c) < 0 or int(c) >= len(grid[0]):
                return 
            if grid[r][c] == "1":
                grid[r][c] = "0"
                explore_island(r+1, c)
                explore_island(r-1, c)
                explore_island(r, c-1)
                explore_island(r, c+1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    island_count += 1
                    explore_island(r, c)
        return island_count
