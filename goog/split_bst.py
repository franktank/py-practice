def helper(root, threshold:
  if not root:
    return None, None
  if root.val > threshold:
    left, right = self.helper(node.left, threshold)
    root.left = right
    return left, root
  else:
    left, right = self.helper(root.right, threshold)
    root.right = left
    return root, right
