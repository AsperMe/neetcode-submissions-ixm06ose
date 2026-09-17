class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        result = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    result += 4
                    if r and grid[r - 1][c]:
                        result -= 2
                    if c and grid[r][c - 1] == 1:
                        result -= 2
        return result