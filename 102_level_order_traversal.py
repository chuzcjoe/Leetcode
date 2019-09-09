# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

        
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return
        
        array = []
        
        queue = [root]
        
        while queue:
            array.append([node.val for node in queue])
            queue = [node for val in queue if val 
                            for node in [val.left,val.right] if node]
        
        return array
        
        
        