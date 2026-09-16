class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n, result = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    result += (i+1 >= m or grid[i+1][j] == 0)
                    result += (j+1 >= n or grid[i][j+1] == 0)
                    result += (i-1 < 0 or grid[i-1][j] == 0)
                    result += (j-1 < 0 or grid[i][j-1] == 0)
        return result            