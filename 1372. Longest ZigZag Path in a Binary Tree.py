# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        
        
        #dfs returns the longest left zigzag and right zigzag and longest zigzag stating at root
        def dfs(node):
            if not node:
                return [0,0,0]
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            return [left[1]+1, right[0]+1, max(left[1]+1, right[0]+1, left[2], right[2])]
        
        return dfs(root)[-1]-1