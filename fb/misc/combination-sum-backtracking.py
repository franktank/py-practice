class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.helper(candidates, [], target, 0)
        return self.res

    def helper(self, candidates, cur_comb, target, start):
        if target < 0:
            return # BUST
        elif target == 0:
            # Found target
            self.res.append(list(cur_comb))
        else:
            for i in range(start, len(candidates)):
                cur_comb.append(candidates[i])
                self.helper(candidates, cur_comb, target-candidates[i], i)
                cur_comb.pop() # the last dude made it bust
