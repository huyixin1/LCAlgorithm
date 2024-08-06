# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return self.res
        q = [root]

        while q:
            sz = len(q)
            layer = []
            for i in range(sz): # each layer
                cur = q.pop(0) # from left to right
                layer.append(cur.val)
                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
            self.res.append(layer)
        return self.res
