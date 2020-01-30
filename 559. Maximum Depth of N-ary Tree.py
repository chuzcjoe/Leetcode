"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        
        def dfs(root):
            if not root:
                return 0
            
            if not root.children:
                return 1
            
            return max([dfs(node) for node in root.children]) + 1
        
        return dfs(root)
        