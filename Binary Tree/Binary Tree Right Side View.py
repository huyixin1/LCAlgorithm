# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # find rightest node in each layer
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None:
            return res
        q = [root]
        while q:
            sz = len(q)
            layer = []
            for i in range(sz):
                cur = q.pop(0)
                layer.append(cur.val)
                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
            res.append(layer.pop())
        return res