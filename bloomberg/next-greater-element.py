class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        stack = []
        for num in nums:
            while stack and num > stack[len(stack)-1]:
                d[stack.pop()] = num
            stack.append(num)


        res = []
        for i in range(len(findNums)):
            if findNums[i] in d:
                res.append(d[findNums[i]])
            else:
                res.append(-1)
        return res
