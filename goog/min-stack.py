class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        cur_min = self.getMin()
        if not cur_min == None:
            cur_min = min(cur_min, x)
            self.stack.append([x, cur_min])
        else:
            self.stack.append([x, x])

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop(len(self.stack)-1)

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[len(self.stack)-1][0]
        return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[len(self.stack)-1][1]
        return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
