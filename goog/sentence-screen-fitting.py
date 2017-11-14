class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        dp = [[-1 for _ in range(len(sentence))] for _ in range(len(cols))]
        self.helper(dp, sentence, 0, 0, rows, cols, 0)
        return dp[0][0]

    def helper(self, dp, sentence, cur_row, cur_row_letters, rows, cols, cur_word):
        if not dp[cur_row_letters][cur_word] == -1:
            return dp[cur_row_letters][cur_word]
        if cur_word >= len(sentence):
            dp[cur_row_letters][cur_word] = 1 + self.helper(dp, sentence, cur_row, cur_row_letters, rows, cols, 0)
            return dp[cur_row_letters][cur_word]
        if cur_row >= rows:
            return 0
        if cur_row_letters + len(sentence[cur_word]) < cols:
            dp[cur_row_letters][cur_word] = self.helper(dp, sentence, cur_row, cur_row_letters + len(sentence[cur_word]), rows, cols, cur_word + 1)
        else:
            dp[cur_row_letters][cur_word] = self.helper(dp, sentence, cur_row + 1, 0, rows, cols, cur_word)

class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        self.num_sentence = 0
        self.helper(sentence, 0, 0, rows, cols, 0)
        return self.num_sentence

    def helper(self, sentence, cur_row, cur_row_letters, rows, cols, cur_word):
        if cur_word >= len(sentence):
            self.num_sentence += 1
            self.helper(sentence, cur_row, cur_row_letters, rows, cols, 0)
            return
        if cur_row >= rows:
            return
        if cur_row_letters + len(sentence[cur_word]) < cols:
            cur_row_letters += len(sentence[cur_word])
            self.helper(sentence, cur_row, cur_row_letters, rows, cols, cur_word + 1)
        else:
            self.helper(sentence, cur_row + 1, 0, rows, cols, cur_word)
