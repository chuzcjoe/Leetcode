# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        
        
        def dfs(node):
            if not node:
                return 0, None
            
            h1, nxt1 = dfs(node.left)
            h2, nxt2 = dfs(node.right)
            
            if h1 > h2:
                return h1 + 1, nxt1
            elif h1 < h2:
                return h2 + 1, nxt2
                
            
            return h1+1, node 
            
        
        depth, ans = dfs(root)
        return ans
        