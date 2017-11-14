class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = self.dfs(i,j,grid)
                    m = max(m,area)
        return m

    def dfs(self,row, col, grid):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
            return 0
        else:
            grid[row][col] = 0
            return 1 + self.dfs(row + 1,col,grid) + self.dfs(row - 1,col,grid) + self.dfs(row,col+1,grid) + self.dfs(row,col-1,grid)
