class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        self.max = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.helper(matrix, i, j, -sys.maxint, 0)
        return self.max

    def helper(self, matrix, row, col, prev, cur_len):
        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or matrix[row][col] <= prev:
            return
        else:
            cur_len += 1
            self.max = max(self.max, cur_len)
            self.helper(matrix, row+1, col, matrix[row][col], cur_len)
            self.helper(matrix, row-1, col, matrix[row][col], cur_len)
            self.helper(matrix, row, col+1, matrix[row][col], cur_len)
            self.helper(matrix, row, col-1, matrix[row][col], cur_len)


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = 0
        dp = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                m = max(m, self.helper(dp, matrix, i, j, -sys.maxint))
        return m

    def helper(self, dp, matrix, row, col, prev):
        if not dp[row][col] == -1:
            return dp[row][col]
        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or matrix[row][col] <= prev:
            dp[row][col] = 0
            return 0
        else:
            bottom = 1 + self.helper(matrix, row+1, col, matrix[row][col])
            top = 1 + self.helper(matrix, row-1, col, matrix[row][col])
            right = 1 + self.helper(matrix, row, col+1, matrix[row][col])
            left = 1 + self.helper(matrix, row, col-1, matrix[row][col])
            dp[row][col] = max(bottom, top, left, right)
            return dp[row][col]
