# Brute Force
class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.max = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.helper(grid, i, j)
        return self.max

    def helper(self, grid, row, col):
        if not grid[row][col] == '0':
            return
        count = 0
        for i in range(row-1,-1,-1):
            if grid[i][col] == 'W':
                break
            if grid[i][col] == 'E':
                count += 1
        for i in range(row+1,len(grid)):
            if grid[i][col] == 'W':
                break
            if grid[i][col] == 'E':
                count += 1

        for i in range(col-1,-1,-1):
            if grid[row][i] == 'W':
                break
            if grid[row][i] == 'E':
                count += 1

        for i in range(col+1,len(grid[0])):
            if grid[row][i] == 'W':
                break
            if grid[row][i] == 'E':
                count += 1
        self.max = max(self.max, count)

# DP
class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        row = 0
        columns = [0 for _ in range(len(grid[0]))]
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'W':
                    continue
                if j == 0 or grid[i][j-1] == 'W':
                    row = self.search_row(grid, i, j)
                if i == 0 or grid[i-1][j] == 'W':
                    columns[j] = self.search_col(grid, i, j)
                if grid[i][j] == '0':
                    res = max(res, columns[j] + row)
        return res

    def search_row(self, grid, row, col):
        res = 0
        while col < len(grid[0]) and not grid[row][col] == 'W':
            if grid[row][col] == 'E':
                res += 1
            col += 1
        return res

    def search_col(self, grid, row, col):
        res = 0
        while row < len(grid) and not grid[row][col] == 'W':
            if grid[row][col] == 'E':
                res += 1
            row += 1
        return res
