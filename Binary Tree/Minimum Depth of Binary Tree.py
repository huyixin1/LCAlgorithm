# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)

        if leftDepth == 0:
            return rightDepth + 1

        if rightDepth == 0:
            return leftDepth + 1

        return min(leftDepth, rightDepth) +1