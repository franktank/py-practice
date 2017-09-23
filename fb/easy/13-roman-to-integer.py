"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        special = {}
        normal = {}
        special['IV'] = 4
        special['IX'] = 9
        special['XL'] = 40
        special['XC'] = 90
        special['CD'] = 400
        special['CM'] = 900

        normal['I'] = 1
        normal['V'] = 5
        normal['X'] = 10
        normal['L'] = 50
        normal['C'] = 100
        normal['D'] = 500
        normal['M'] = 1000

        ret = 0
        i = 0
        while i < len(s) - 1:
            curr = s[i] + s[i + 1]
            if curr in special:
                ret += special[curr]
                i += 2
            else:
                ret += normal[s[i]]
                i += 1
            print(i)
        if i < len(s):
            ret += normal[s[i]]
        return ret
"""
Map normal and special cases
Use index i to traverse through string while i < len(s) - 1
    If special increment i by 2
    If normal increment i by 1
After iteration
if i < len(s):
    last character not accounted for
    add value from last char to result
Return result
"""
