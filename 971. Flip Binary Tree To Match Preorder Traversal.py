# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        
        def dfs(node, voyage):
            nonlocal res, cnt
            
            if not node:
                return True
            
            if node.val != voyage[cnt]:
                return False
            
            cnt += 1
            
            
            if node.left and node.left.val != voyage[cnt]:
                res.append(node.val)
                node.left, node.right = node.right, node.left
            
            return dfs(node.left, voyage) and dfs(node.right, voyage)
        
        res = []
        cnt = 0
        
        return res if dfs(root, voyage) else [-1]
            
            
            
            
        