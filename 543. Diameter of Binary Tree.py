# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        #dfs used for calculating the deepest path of subtree
        def dfs(node):
            nonlocal longest
            
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            longest = max(longest, left+right)
            
            return 1 + max(left, right)
        
        longest = 0
        print(dfs(root))
        
        return longest
        
            
            
            
        