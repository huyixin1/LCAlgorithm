# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # cross-traverse value
        # upper and lower zone
        def check(node, low, high):
            if node is None: return True
            # judge if left subtree is valid
            if node.val <= low or node.val >= high:
                return False
            if check(node.left, low, node.val) is False:
                return False
            # judge if right subtree is valid
            if check(node.right, node.val, high) is False:
                return False
            return True

        return check(root, float('-inf'), float('inf'))