# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        res = []
        
        def dfs(node, prev, depth, target):
            if not node:
                return
            if node.val == target:
                res.append([prev, depth])
            
            dfs(node.left, node.val, depth+1, target)
            dfs(node.right, node.val, depth+1, target)
        
        dfs(root, None, 0, x)
        dfs(root, None, 0, y)
        
        c1, c2 = res
        if c1[0] != c2[0] and c1[1] == c2[1]:
            return True
        else:
            return False
                
            
        
        