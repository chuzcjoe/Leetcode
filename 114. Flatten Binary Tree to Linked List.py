# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        nodes = []
        
        def dfs(root):
            
            if not root:
                return
            
            nodes.append(root)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        for i in range(len(nodes)-1):
            nodes[i].left = None
            nodes[i].right = nodes[i+1]
        
        