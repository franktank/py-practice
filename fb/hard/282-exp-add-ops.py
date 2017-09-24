"""
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Examples:
"123", 6 -> ["1+2+3", "1*2*3"]
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
"""
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        OPERATORS = ["-", "+", "*", ""]
        res = []
        res.append(num[0])
        for i in range(1, len(num) - 1):
            new_list = []
            for j in range(len(res)):
                for operator in OPERATORS:
                    new_list.append(res[j] + operator + num[i])
            res = list(new_list)
        for e in res:
            e + num[len(num)-1]
        ret = []
        for e in res:
            if eval(e) == target
                ret.append(e)
        return ret

# DFS
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if not num:
            return list()
        self.target = target
        self.res = []
        self.dfs(num[1:], str(num[0]), int(num[0]), int(num[0]))
        return self.res

    def dfs(self, num, s, val, prev_val):
        if not num:
            if val == self.target:
                self.res.append(s)
            return
        self.dfs(num[1:], s + "+" + str(num[0]), val + int(num[0]), int(num[0]))
        self.dfs(num[1:], s + "*" + str(num[0]), val - prev_val + prev_val * int(num[0]), prev_val*int(num[0]))
        self.dfs(num[1:], s + "-" + str(num[0]), val - int(num[0]), -int(num[0]))
        if not s[len(s)-1] == '0':
            self.dfs(num[1:], s + "" + str(num[0]), eval(s + "" + str(num[0])), int(str(prev_val)+str(num[0])))
