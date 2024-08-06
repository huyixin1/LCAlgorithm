# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        
        # revert left and right subtree
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left, root.right = right, left # root.left, root.right we want to exchange subtree

        return root