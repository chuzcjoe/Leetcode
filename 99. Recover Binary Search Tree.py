# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        vals = []
        
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            vals.append(root.val)
            inorder(root.right)
        
        inorder(root)
        
        tmp = sorted(vals)
        swap = {}
        
        for x,y in zip(tmp, vals):
            if x != y:
                swap[x] = y
                swap[y] = x
        
        def dfs(root):
            if not root:
                return
            
            if root.val in swap:
                root.val = swap[root.val]
            
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        
        
                
        