class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        m = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        } 
        res = [""]
        q = []
        for digit in digits:
            new_res = []
            for c in m[digit]:
                for e in res:
                    new_res.append(c + e)
            res = new_res
        return res
