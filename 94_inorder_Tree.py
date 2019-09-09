# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def __init__(self):
        self.array = []
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if not root:
            return
        
        
        self.inorderTraversal(root.left)
        self.array.append(root.val)
        self.inorderTraversal(root.right)
        
        return self.array
        