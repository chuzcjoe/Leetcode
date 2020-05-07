# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
    
        def dfs(s, t):
            if not s and not t:
                return True
            
            if not s or not t or s.val != t.val:
                return False
            
            left = dfs(s.left, t.left)
            right = dfs(s.right, t.right)
            
            return left and right
        
        
        
        def find(s, t):
            nonlocal sub
            if sub or not s:
                return
            
            if s.val == t.val:
                sub = dfs(s, t)
            
            find(s.left, t)
            find(s.right, t)
        
        sub = False
        find(s, t)
        return sub