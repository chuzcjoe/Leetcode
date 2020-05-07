# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        
        """
        My solution
        def dfs(ancestor_val, node, depth):
            nonlocal MAX
            
            if not node:
                return
            
            if depth >= 1:
                MAX = max(abs(ancestor_val-node.val), MAX)
            
            dfs(ancestor_val, node.left, depth+1)
            dfs(ancestor_val, node.right, depth+1)
        
        def find(node):
            if not node:
                return
            
            dfs(node.val, node, 0)
            find(node.left)
            find(node.right)
        
        
        MAX = 0
        find(root)
        return MAX
        """
        
        """
        DALAO solution
        """
        
        def dfs(MAX, MIN, node):
            nonlocal res
            
            if not node:
                return
            
            MAX = max(MAX, node.val)
            MIN = min(MIN, node.val)
            if not node.left and not node.right:
                res = max(res, abs(MAX-MIN))
            
            dfs(MAX, MIN, node.left)
            dfs(MAX, MIN, node.right)
        
        res = 0
        dfs(-float('inf'), float('inf'), root)
        return res
                
            
            
            
            
             
            