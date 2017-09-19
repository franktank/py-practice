"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""
class Solution(object):
    # O(kn^2) solution
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k == 0 or len(prices) == 0:
            return 0

        dp = [[0 for _ in range(len(prices))] for _ in range(k + 1)]

        for i in range(1, k + 1):
            for j in range(1, len(prices)):
                max_val = 0
                for m in range(0, j):
                    max_val = max(max_val, prices[j] - prices[m] + dp[i-1][m])
                dp[i][j] = max(max_val, dp[i][j-1])
        print(dp)
        return dp[k][len(prices) - 1]

    # optimization O(kn) Solution
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k == 0 or len(prices) == 0:
            return 0
        if k >= len(prices):
            return self.unlimited(prices)
        dp = [[0 for _ in range(len(prices))] for _ in range(k + 1)]
        for i in range(1, k + 1):
            # running index tracking prev max profit to get rid of for loop bc of associate and commutative properties of addition
            max_profit = -prices[0]
            for j in range(1, len(prices)):
                max_profit = max(max_profit, dp[i-1][j-1] - prices[j-1])
                dp[i][j] = max(dp[i][j-1], prices[j] + max_profit)
        print(dp)
        return dp[k][len(prices) - 1]

        # optimization linear space complexity but still O(kn)
        def maxProfit(self, k, prices):
            """
            :type k: int
            :type prices: List[int]
            :rtype: int
            """
            if k == 0 or len(prices) == 0:
                return 0

            if k >= len(prices):
                return unlimited(prices)

            dp = [0 for _ in range(len(prices))]
            dp_prev = [0 for _ in range(len(prices))]
            for i in range(1, k + 1):
                max_profit = -prices[0]
                for j in range(1, len(prices)):
                    max_profit = max(max_profit, dp_prev[j-1] - prices[j-1])
                    dp[j] = max(dp[j-1], prices[j] + max_profit)
                dp_prev = list(dp)
            print(dp)
            return dp[len(prices) - 1]

        def unlimited(self, prices):
            profit = 0
            for i in range(1, len(prices)):
                if prices[i-1] < prices[i]:
                    profit += prices[i] - prices[i-1]
            return profit
