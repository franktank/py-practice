class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        dp = [[-1 for _ in range(len(matrix[0]))]for _ in range(len(matrix))]
        m = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = self.helper(matrix, i, j, matrix[i][j]-1, dp)
                m = max(m, res)
        return m

    def helper(self, matrix, row, col, prev, dp):
        # Check borders
        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or matrix[row][col] <= prev:
            return 0
        if not dp[row][col] == -1:
            return dp[row][col]
        else:
            top = 1 + self.helper(matrix, row-1, col, matrix[row][col], dp)
            down = 1 + self.helper(matrix, row+1, col, matrix[row][col], dp)
            left = 1 + self.helper(matrix, row, col-1, matrix[row][col], dp)
            right = 1 + self.helper(matrix, row, col+1, matrix[row][col], dp)
            dp[row][col] = max(top,down,left,right)
            return dp[row][col]
