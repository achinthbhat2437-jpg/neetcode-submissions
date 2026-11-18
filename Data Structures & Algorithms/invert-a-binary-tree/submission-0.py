# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if(root==None):
            return root
        p = root
        q = p.left
        p.left = p.right
        p.right = q
        if(p.left!=None):
           self.invertTree(p.left)
        if(p.right!=None):
            self.invertTree(p.right)
        return root
        
        
        
        
