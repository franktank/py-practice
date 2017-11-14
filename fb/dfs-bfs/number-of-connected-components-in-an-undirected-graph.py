class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        self.islands = [i for i in range(n)]
        for edge in edges:
            find_x = self.find_parent(edge[0])
            find_y = self.find_parent(edge[1])

            self.islands[find_y] = find_x

        return len(set(self.islands))

    def find_parent(self, element):
        if self.islands[element] = element:
            return element
        return find_parent(self.islands[element])
