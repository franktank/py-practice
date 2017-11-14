class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.cols = {}
        self.bfs(root)
        keys = list(self.cols.keys())
        keys.sort()
        res = []
        for key in keys:
            res.append(self.cols[key])
        return res

    def bfs(self, root):
        q = []
        q.append([0, root])
        while q:
            cur = q.pop(0)
            if cur[0] in self.cols:
                self.cols[cur[0]].append(cur[1].val)
            else:
                self.cols[cur[0]] = [cur[1].val]
            if cur[1].left:
                q.append([cur[0]-1, cur[1].left])
            if cur[1].right:
                q.append([cur[0]+1, cur[1].right])
