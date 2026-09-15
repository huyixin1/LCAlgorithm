# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # the longest path (diameter) might pass through nodes other than the root.
    def __init__(self):
        self.diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def maxDepth(root):           
            if root is None:
                return 0
            
            left_depth = maxDepth(root.left)
            right_depth = maxDepth(root.right)
            # Update the diameter if the path through this node is larger
            self.diameter = max(left_depth+right_depth, self.diameter)
            # return the depth of (root)tree 
            return max(left_depth,right_depth) + 1

        maxDepth(root)
        return self.diameter