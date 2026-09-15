# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self,root):
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        if left_depth < 0 or right_depth < 0 or abs(left_depth-right_depth) > 1: # any of the subtrees themselves are unbalanced
            return -1
        return max(left_depth, right_depth) + 1 # subtree depth
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = self.maxDepth(root)
        return (res >= 0)