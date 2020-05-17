# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        
        def dfs(node, max_value):
            nonlocal cnt
            if not node:
                return
            
            if max_value <= node.val:
                cnt += 1
            
            max_value = max(node.val, max_value)
            
            dfs(node.left, max_value)
            dfs(node.right, max_value)
        
        cnt = 0
        
        dfs(root, -float('inf'))
        return cnt