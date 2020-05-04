# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        
        
        def dfs(prev, node, left):
            nonlocal res
            
            if not node:
                return
            
            if node.val in to_delete:
                if node in res:
                    res.remove(node)
                    
                if prev:
                    if left:
                        prev.left = None
                    else:
                        prev.right = None

                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)
            
            dfs(node, node.left, True)
            dfs(node, node.right, False)
        
        res = [root]
        dfs(None, root, True)
        
        return res