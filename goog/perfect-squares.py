import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares = []
        i = 1
        while True:
            if i*i <= n:
                squares.append(i*i)
            i += 1

        paths = []
        height = 0
        paths.append(n)
        while True:
            height += 1
            new_paths = []
            for path in paths:
                for square in squares:
                    val = path - square
                    if val == 0:
                        return height
                    new_paths.append(val)
            paths = new_paths
