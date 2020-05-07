# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        """
        1.BFS
        
        if not root:
            return 0
        
        leaves = []
        level = [root]
        while level:
            
            for node in level:
                if node.left and not node.left.left and not node.left.right:
                    leaves.append(node.left.val)
            
            level = [child for node in level for child in [node.left, node.right] if child]
        
        return sum(leaves)
        """
        
    
        
        """
        2.DFS
        """
        
        def dfs(node):
            
            if not node:
                return 0
            
            if node.left and not node.left.left and not node.left.right:
                return node.left.val + dfs(node.right)
            
            return dfs(node.left) + dfs(node.right)
        
        return dfs(root)
        