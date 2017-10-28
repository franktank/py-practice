class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.helper(candidates, target, 0, [])
        return self.res

    def helper(self, candidates, target, start_index, path):
        if target < 0:
            return
        elif target == 0:
            self.res.append(list(path))
        else:
            for i in range(start_index, len(candidates)):
                path.append(candidates[i])
                self.helper(candidates,target-candidates[i], i, path)
                path.pop()
