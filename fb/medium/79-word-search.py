"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # Some kinda DFS like islands
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    res = self.dfs(board, i, j, word)
                    if res:
                        return True
        return False

    def dfs(self, board, row, col, word):
        if len(word) == 0:
            return True
        if row < 0 or row > (len(board) - 1) or col < 0  or col > (len(board[0]) - 1) or not word[0] == board[row][col]:
            return False
        mem = board[row][col]
        board[row][col] = "."
        res = self.dfs(board, row+1, col, word[1:]) or self.dfs(board, row-1, col, word[1:]) or self.dfs(board, row, col-1, word[1:]) or self.dfs(board, row, col+1, word[1:])
        board[row][col] = mem
        return res
"""
DFS
SIMILAR TO NUMBER OF ISLANDS
OR OPERATOR!!!!
DFS UNTIL EITHER WORD DOESNT EXIST OR LEN(WORD) PASSES IN IS 0
BACKTRACK BOARD
"""
