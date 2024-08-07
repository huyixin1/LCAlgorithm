# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    index_to_val = dict() # hashmap to store num
    def build(self,preorder, prestart, preend, inorder, instart, inend):
        if prestart > preend:
            return None # preorder and inorder list should be same

        root_val = preorder[prestart]
        
        root_index = self.index_to_val[root_val] # get the index of root
        leftsz = root_index - instart
        rightsz = inend - root_index
        # prestart += 1 will change the state directly
        root = TreeNode(root_val) # construct root node
        root.left = self.build(preorder, prestart + 1, prestart + leftsz, inorder, instart, root_index - 1)
        root.right = self.build(preorder, prestart + leftsz + 1, preend, inorder, root_index + 1, inend)
        return root
        

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        for i in range(len(inorder)):
            self.index_to_val[inorder[i]] = i
        return self.build(preorder,0, len(preorder)-1, inorder, 0, len(inorder)-1)
        