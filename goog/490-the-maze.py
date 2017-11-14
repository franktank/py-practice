class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        return self.helper(maze, start[0], start[1], destination)

    def helper(self, maze, row, col, destination):
        if row < 0 or row >= len(maze) or col < 0 or col >= len(maze[0]) or maze[row][col] == 1:
            return False
        if row == destination[0] and col == destination[1]:
            if not self.helper(maze, row-1, col, destination) and not self.helper(maze, row+1, col, destination) and not self.helper(maze, row, col-1, destination) and not self.helper(maze, row, col+1, destination):
                return True
        else:
            maze[row][col] = 1
            res = self.helper(maze, row-1, col, destination) or self.helper(maze, row+1, col, destination) or self.helper(maze, row, col-1, destination) or self.helper(maze, row, col+1, destination)
            maze[row][col] = 0
            return res
