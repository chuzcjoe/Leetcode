# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        
        """
        My solution
        
        def dfs(node, prev_node, flg, target):
            if not node:
                return
            
            if node.val == target and not node.left and not node.right:
                if flg:
                    prev_node.left = None
                else:
                    prev_node.right = None
                
                if not prev_node.left and not prev_node.right and prev_node.val == target:
                    dfs(root, dummy, True, target)
            
            dfs(node.left, node, True, target)
            dfs(node.right, node, False, target)
        
        dummy = TreeNode(None)
        dummy.left = root
        dfs(root, dummy, True, target)
        
        return dummy.left
        """
        
        """
        DALAO solution
        """
        
        def dfs(node, target):
            if not node:
                return
            
            node.left = dfs(node.left, target)
            node.right = dfs(node.right, target)
            if node.val == target and not node.left and not node.right:
                return None
            
            return node
        
        return dfs(root, target)
        
                
        