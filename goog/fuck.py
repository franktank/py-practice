class TreeNode:
    def __init__(val):
        self.val = val
        self.left = None
        self.right = None

global_m = 0
def solution(A, E):
    nodes = {}
    for i in range(0, len(E), 2):
        parent = E[i]
        child = E[i+1]

        if parent in nodes:
            p = nodes[parent]
        else:
            nodes[parent] = TreeNode(A[parent-1])
            p = nodes[parent]

        if child in nodes:
            c = nodes[child]
        else:
            nodes[child] = TreeNode(A[child-1])
            c = nodes[child]

        if child = 2*parent:
            p.left = c
        else:
            p.right = c


    root = nodes[1]
    longest_path(root, root.val)

def longest_path(root, prev):
    if not root:
        return 0
    if not root.val == prev:
        return 0
    l = longest_path(root.left, root.val)
    r = longest_path(root.right, root.val)

    m = max(l,r) + 1
    global_m = max(global_m, m)
    return m
