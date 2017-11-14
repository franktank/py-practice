class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                res = dfs(board, word, i, j)
                if res:
                    return True
        return False
    def dfs(self, board, word, row, col):
        if len(word) == 0:
            return True
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or not board[row][col] == word[0]:
            return False

        # Replace current letter temporarily to prevent reuse
        temp = board[row][col]
        board[row][col] = "."
        # Now we search again for next letter
        res = self.dfs(board, word[1:], row + 1, col) or self.dfs(board, word[1:], row - 1, col) or self.dfs(board, word[1:], row, col + 1) or self.dfs(board, word[1:], row, col - 1)
        board[row][col] = temp
        return res
