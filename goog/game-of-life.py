class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        copy = [[None for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                live = self.check_adjacent(board, i, j)
                print(live)
                if board[i][j] == 1:
                    if live < 2 or live> 3:
                        copy[i][j] = 0
                    else:
                        copy[i][j] = 1
                else:
                    if live == 3:
                        copy[i][j] = 1
                    else:
                        copy[i][j] = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = copy[i][j]

    def check_adjacent(self,board,row,col):
        count_live = 0
        for i in range(row-1,row+2):
            for j in range(col-1, col+2):
                if i == row and j == col:
                    continue
                count_live += self.border(board, i, j)
        return count_live


    def border(self, board, row, col):
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            return 0
        return board[row][col]
