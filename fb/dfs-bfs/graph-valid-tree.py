"""
Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.
"""
# Search
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        parents = [None for _ in range(n)]


# Union Find
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        islands = [i for i in range(n)]
        for edge in edges:
            find_x = find_parent(edge[0])
            find_y = find_parent(edge[1])

            if (find_x == find_y):
                return False # CYCLE because they're in same set already

            islands[find_y] = find_x
        return edge.length == n-1

    def find_parent(self, element):
        if islands[element] == element:
            return element
        return find_parent(num[element])
