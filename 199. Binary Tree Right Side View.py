# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        """
        if not root:
            return []
        
        level = [root]
        res = []
        
        
        while level:
            
            res.append(level[-1].val)
            
            level = [child for node in level for child in (node.left, node.right) if child]
        
        return res
        """
        
        def dfs(node, depth):
            
            if node:
                if depth == len(res):
                    res.append(node.val)
                
                dfs(node.right, depth + 1)
                dfs(node.left, depth + 1)
        
        
        res = []
        dfs(root, 0)
        
        return res