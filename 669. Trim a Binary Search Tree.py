# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        
        def dfs(node, L, R):
            
            if not node:
                return
            
            if node.val < L:
                return dfs(node.right, L, R)
            if node.val > R:
                return dfs(node.left, L, R)
            
            node.left = dfs(node.left, L, R)
            node.right = dfs(node.right, L, R)
            
            return node
        
        return dfs(root,L,R)
            
            
        