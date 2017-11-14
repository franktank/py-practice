class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        pv = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        av = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        for i in range(len(matrix)):
            self.helper(matrix, pv, i, 0)
            self.helper(matrix, av, i, len(matrix[0]) - 1)

        for i in range(len(matrix[0])):
            self.helper(matrix, pv, 0, i)
            self.helper(matrix, pv, len(matrix), i)

        res = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if pv[i][j] == av[i][j]
                    res.append([i, j])

        return res

    def helper(self, matrix, visited, row, col, prev_val):
        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or prev_val < matrix[row][col] or visited[row][col] == True:
            return
        visited[row][col] = True
        self.helper(matrix, visited, row + 1, col, matrix[row][col])
        self.helper(matrix, visited, row - 1, col, matrix[row][col])
        self.helper(matrix, visited, row, col + 1, matrix[row][col])
        self.helper(matrix, visited, row, col - 1, matrix[row][col])

class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return list()
        pv = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        av = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        for i in range(len(matrix)):
            self.helper(matrix, pv, i, 0, matrix[i][0])
            self.helper(matrix, av, i, len(matrix[0]) - 1, matrix[i][len(matrix[0])-1])

        for i in range(len(matrix[0])):
            self.helper(matrix, pv, 0, i, matrix[0][i])
            self.helper(matrix, av, len(matrix) - 1, i, matrix[len(matrix)-1][i])

        res = []
        print(av)
        print(pv)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if pv[i][j] and av[i][j]:
                    res.append([i, j])

        return res

    def helper(self, matrix, visited, row, col, prev_val):
        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or prev_val < matrix[row][col] or visited[row][col] == True:
            return
        visited[row][col] = True
        self.helper(matrix, visited, row + 1, col, matrix[row][col])
        self.helper(matrix, visited, row - 1, col, matrix[row][col])
        self.helper(matrix, visited, row, col + 1, matrix[row][col])
        self.helper(matrix, visited, row, col - 1, matrix[row][col])
