# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        
        def getD(s):
            nonlocal i
            d = 0
            while i < len(s) and s[i] == '-':
                d += 1
                i += 1
            return d
        
        def getV(s):
            nonlocal i
            v = ""
            while i < len(s) and s[i].isdigit():
                v += s[i]
                i += 1
            
            return int(v)
        
        def dfs(s, depth):
            nonlocal i
            d = getD(s)
            if d != depth:
                i -= d
                return
            
            root = TreeNode(getV(s))
            root.left = dfs(s, depth+1)
            root.right = dfs(s, depth+1)
            
            return root
        
        i = 0
        root = dfs(S, 0)
        
        return root