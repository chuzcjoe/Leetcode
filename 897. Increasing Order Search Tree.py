# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        nodes = []
        
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            nodes.append(root)
            dfs(root.right)
        
        dfs(root)
        
        for i in range(len(nodes)-1):
            nodes[i].left = None
            nodes[i].right = nodes[i+1]
        
        return nodes[0]
        