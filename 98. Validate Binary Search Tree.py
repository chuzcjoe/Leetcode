# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        1. recursive
        
        def valid(root, MAX, MIN):
            if not root:
                return True
            
            if root.val >= MAX or root.val <= MIN:
                return False
            
            l = valid(root.left, min(MAX, root.val), MIN)
            r = valid(root.right, MAX, max(MIN, root.val))
            
            return l&r
        
        return valid(root, float('inf'), -float('inf'))
        """
        
        #2. inorder
        
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            vals.append(root.val)
            inorder(root.right)
        
        def valid(root, vals):
            
            for i in range(len(vals)-1):
                if vals[i] >= vals[i+1]:
                    return False
            
            return True
        
        vals = []
        inorder(root)
        
        return valid(root, vals)
            
        