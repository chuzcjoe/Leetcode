# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        def dfs(preorder, inorder):
            if not preorder or not inorder:
                return None
            
            root = TreeNode(preorder[0])
            i = inorder.index(preorder[0])
            
            root.left = dfs(preorder[1:i+1], inorder[:i])
            root.right = dfs(preorder[i+1:], inorder[i+1:])
            
            return root
        
        return dfs(preorder, inorder)