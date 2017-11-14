class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        return self.helper(matrix, target, 0, 0)

    def helper(self, matrix, target, row, col):
        if row >= len(matrix) or col >= len(matrix[0]) or matrix[row][col] > target:
            return False
        elif matrix[row][col] == target:
            return True
        else:
            return self.helper(matrix, target, row+1, col) or self.helper(matrix, target, row, col+1)

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row = 0
        col = len(matrix[0])-1

        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False
