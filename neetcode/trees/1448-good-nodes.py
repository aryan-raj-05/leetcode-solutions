# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(root, curr):
            if not root:
                return

            if root.val >= curr:
                self.count += 1
                curr = root.val

            dfs(root.left, curr)
            dfs(root.right, curr)

        dfs(root, root.val)

        return self.count
