# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        def traverse(node):
            nonlocal max_diameter
            if node is None: return 0
            left_h = traverse(node.left)
            right_h = traverse(node.right)
            max_diameter = max(max_diameter, left_h + right_h) # update the diameter in each node
            return max(left_h, right_h) + 1

        # left_height = traverse(root.left)
        # right_height = traverse(root.right)
        # diameter = left_height + right_height
        # max_diameter = max(max_diameter, diameter)
        # double calculate the diameter through root
        traverse(root)

        return max_diameter