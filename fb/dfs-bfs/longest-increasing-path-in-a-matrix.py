class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        self.max_path = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.dfs(matrix, i, j, 0, -1)
        return self.max_path

    def dfs(self, matrix, row, col, prev):
        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or matrix[row][col] <= prev:
            return
        self.max_path = max(self.max_path, cur_path_len + 1)
        self.dfs(matrix, row+1, col, cur_path_len + 1, matrix[row][col])
        self.dfs(matrix, row-1, col, cur_path_len + 1, matrix[row][col])
        self.dfs(matrix, row, col+1, cur_path_len + 1, matrix[row][col])
        self.dfs(matrix, row, col-1, cur_path_len + 1, matrix[row][col])

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # Memoize!
        if not matrix:
            return 0
        self.memo = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        res = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, self.dfs(matrix, i, j, -1))
        return res

    def dfs(self, matrix, row, col, prev):
        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or matrix[row][col] <= prev:
            return 0
        if not self.memo[row][col] == 0:
            return self.memo[row][col]
        a = 1 + self.dfs(matrix, row+1, col, matrix[row][col])
        b = 1 + self.dfs(matrix, row-1, col, matrix[row][col])
        c = 1 + self.dfs(matrix, row, col+1, matrix[row][col])
        d = 1 + self.dfs(matrix, row, col-1, matrix[row][col])
        cur_max = max(a, b, c, d)
        self.memo[row][col] = cur_max
        return cur_max
