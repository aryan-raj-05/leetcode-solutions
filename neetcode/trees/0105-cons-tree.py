from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        map_inorder = {v: i for i, v in enumerate(inorder)}
        self.pre_idx = 0

        def build(l, r):
            if l > r:
                return

            root_val = preorder[self.pre_idx]
            mid = map_inorder[root_val]
            self.pre_idx += 1

            root = TreeNode(root_val)

            root.left = build(l, mid - 1)
            root.right = build(mid + 1, r)

            return root

        return build(0, len(inorder) - 1)
