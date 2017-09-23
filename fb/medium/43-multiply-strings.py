"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = [0 for i in range(len(num1) + len(num2))]
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                m = int(num1[i]) * int(num2[j])
                ones_pos = i + j + 1
                tens_pos = i + j
                s = m + res[ones_pos]
                res[ones_pos] = s % 10
                res[tens_pos] += s / 10 # +=  because more passes in the future
        ret_str = ''
        print(res)
        for ele in res:
            if not (len(ret_str) == 0 and ele == 0):
                ret_str += str(ele)
        if len(ret_str) == 0:
            return '0'
        else:
            return ret_str

"""
Approach:
NOTE: will iterate from back of numbers so range(len(num1) - 1, -1, -1)
For every pairwise multiplication, there is a ones and tens digit
Create result array of length len(num1) + len(num2)
Will store ones digit in pos i + j + 1, and tens digit in i + j
For every pairwise multiplication, add result_array[i + j + 1] -> previous tens digit

result_array[i + j + 1] = s % 10
result_array[i + j] += s/10 # Save the tens digit, using += because there can be a value already from an earlier pass

When building a string keep length of string 0 is len(str) == 0 and element is 0...
then return '0' if return string length is 0
"""
