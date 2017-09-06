"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
"""
class Solution(object):
    def check_adj(self, grid, row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return
        if grid[row][col] == '0':
            return

        grid[row][col] = '0'

        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if (i == row - 1 and j == col - 1) or (i == row + 1 and j == col + 1) or (i == row - 1 and j == col + 1) or (i == row + 1 and j == col - 1):
                    continue
                self.check_adj(grid, i, j)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    count += 1
                    self.check_adj(grid, i, j)
        return count
