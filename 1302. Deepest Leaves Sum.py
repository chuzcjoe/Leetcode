# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
        
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        cur = [root]
        
        while cur:
            pre, cur = cur, [child for q in cur for child in [q.left, q.right] if child]
        
        return sum([node.val for node in pre])
        