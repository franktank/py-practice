# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        # DFS from node -> neighbors -> neighbors of neighbor
        # Track nodes visited from label
        if not node:
            return None
        stack = []
        visited = {}
        root = UndirectedGraphNode(node.label)
        visited[node.label] = root
        stack.append(node)
        while stack:
            cur = stack.pop()
            cur_copy = visited[cur.label]
            for neighbor in cur.neighbors:
                if neighbor.label in visited:
                    n_copy = visited[neighbor.label]
                else:
                    n_copy = UndirectedGraphNode(neighbor.label)
                    visited[neighbor.label] = n_copy
                    stack.append(neighbor)
                cur_copy.neighbors.append(n_copy)
        return root
