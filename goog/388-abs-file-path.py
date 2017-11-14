class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        stack = []
        paths = input.split("\n")
        res = 0
        for path in paths:
            p = path.replace("\t", "")
            cur_level = (len(path) - len(p))
            while len(stack) > cur_level:
                stack.pop()
            stack.append(p)
            if "." in p: # found file
                cur_len = 0
                for ele in stack:
                    cur_len += len(ele)
                    cur_len += 1
                res = max(res, cur_len-1)
                print(stack)
        return res
