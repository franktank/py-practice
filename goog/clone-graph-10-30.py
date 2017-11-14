# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        clones = {}
        stack = []
        root = node.label
        stack.append(node)
        root = UndirectedGraphNode(node.label)
        clones[node.label] = root
        # how to handle cycles
        while stack:
            cur = stack.pop()
            clone = clones[cur.label]
            for neighbor in cur.neighbors:
                if neighbor.label in clones:
                    clone.neighbors.append(clones[neighbor.label])
                else:
                    stack.append(neighbor)
                    copy = UndirectedGraphNode(neighbor.label)
                    clones[neighbor.label] = copy
                    clone.neighbors.append(copy)
        return root
