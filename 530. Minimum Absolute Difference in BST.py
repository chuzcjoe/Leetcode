# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        
        res = []
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        
        dfs(root)
        
        output = float('inf')
        left = 0
        for right in range(1, len(res)):
            output = min(res[right]-res[left], output)
            left += 1
        
        return output
        