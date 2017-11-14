class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        while not x == 0:
            new_res = (res*10) + (x%10)
            if not (new_res - x%10) // 10 == res:
                return 0
            res = new_res
            x = x//10
        return res

    def reverse(x):
        res = 0
        while not x == 0:
            new_res = (res*10) + (x%10)
            if not (new_res - x%10) // 10 == res:
                return 0
            res = new_res
            x = x//10
        return res
