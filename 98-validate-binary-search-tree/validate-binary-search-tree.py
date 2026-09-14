# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # cross-traverse value
        prev = None
        def traverse(node):
            nonlocal prev
            if node is None: return True
            # judge if left subtree is valid
            if traverse(node.left) is False:
                return False
            # if prev and node.val <= prev: wrong, because when prev is 0 then it's false
            if prev is not None and node.val <= prev:
                return False
            prev = node.val
            # judge if right subtree is valid
            if traverse(node.right) is False:
                return False
            return True

        return traverse(root)