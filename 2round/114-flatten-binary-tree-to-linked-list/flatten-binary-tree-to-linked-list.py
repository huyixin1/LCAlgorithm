# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # the point is find the right most node
        def traverse(node):
            if node is None:
                return
            
            traverse(node.left)
            traverse(node.right)
            nxt = node.right # store the right subtree
            # cur = node.left ❌ what if node left is None
            node.right = node.left # concat the left subtree to right
            node.left = None
            cur = node
            while cur.right:
                cur = cur.right
            
            cur.right = nxt # put the originl right tree to left subtree end
        

        traverse(root)