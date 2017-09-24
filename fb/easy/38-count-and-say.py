"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
"""
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        res = "1"
        for _ in range(n-1):
            new_str = ""
            prev_char = res[0]
            curr_count = 1
            for i in range(1, len(res)):
                if res[i] == prev_char:
                    curr_count += 1
                else:
                    new_str += str(curr_count) + prev_char
                    prev_char = res[i]
                    curr_count = 1
            new_str += str(curr_count) + prev_char
            res = str(new_str)
        return res
"""
Start with initial value of res = "1"
Run _ in range(n-1) times
Index prev_char and curr_count

21
-> reaches 1 but doesn't have code to append one 1 to results
1211
-> why we need to do new_str += str(curr_count) + prev_char outside of loop
"""
