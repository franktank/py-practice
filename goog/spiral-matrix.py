class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        res = []
        row_start, col_start = 0, 0
        row_end, col_end = len(matrix), len(matrix[0])

        while row_start <= row_end and col_start <= col_end:
            # Traverse right
            for i in range(col_start, col_end):
                res.append(matrix[row_start][i])
            row_start += 1

            # Traverse down
            for i in range(row_start, row_end):
                res.append(matrix[i][col_end])
            col_end -= 1

            # Traverse left, need to check rows because row start could potentially remove the row we should check
            if row_start <= row_end:
                for i in range(col_end, col_start, -1):
                    res.append(matrix[row_end][i])
                row_end -= 1

            # Traverse up, check to see if proper column
            if col_start <= col_end:
                for i in range(row_end, row_start, -1):
                    res.append(matrix[i][col_start])
                col_start += 1
        return res
