# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.array = []
    
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if not root:
            return
        
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.array.append(root.val)
        
        return self.array
        