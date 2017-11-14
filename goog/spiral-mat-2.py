class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[None for _ in range(n)]for _ in range(n)]
        cur_num = 1
        row_start = 0
        row_end = n-1
        col_start = 0
        col_end = n-1
        while row_start <= row_end and col_start <= col_end:
            # Traverse right
            for i in range(col_start, col_end+1):
                res[row_start][i] = cur_num
                cur_num += 1
            row_start += 1

            # Traverse down
            for i in range(row_start, row_end+1):
                res[i][col_end] = cur_num
                cur_num += 1
            col_end -= 1

            # Traverse left, but check to see row is proper row
            if row_start <= row_end:
                for i in range(col_end, col_start-1, -1):
                    res[row_end][i] = cur_num
                    cur_num += 1
                row_end -= 1

            # Traverse up, but check to see column is proper
            if col_start <= col_end:
                for i in range(row_end, row_start-1, -1):
                    res[i][col_start] = cur_num
                    cur_num += 1
                col_start += 1
        return res
