"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""
import sys
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_one, buy_two = 0
        sell_one, sell_two = -sys.maxint - 1
        # Running index of top two slopes
        # Build dp table?
        # Find top two profits that don't overlap!
        for prices in prices:
            sell_two = max(sell_two, buy_two + price)
            buy_two = max(buy_two, sell_one - price)
            sell_one = max(sell_one, buy_one + price)
            buy_one = max(buy_one, -price)
        return sell_two
