class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.cur_mat = 0
        self.matrix = []
        if v1:
            self.matrix.append(v1)
        if v2:
            self.matrix.append(v2)

    def next(self):
        """
        :rtype: int
        """
        res = self.matrix[self.cur_mat].pop(0)
        if not self.matrix[self.cur_mat]:
            self.matrix.pop(self.cur_mat)
        self.cur_mat += 1
        if self.cur_mat >= len(self.matrix):
            self.cur_mat = 0
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.matrix
