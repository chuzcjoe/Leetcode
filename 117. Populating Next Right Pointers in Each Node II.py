"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return None
        
        if not root.left and not root.right:
            root.next = None
            return root
        
        level = [root]
        
        while any(level):
            
            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            if len(level) == 1:
                level[-1].next = None
            else:
                for i in range(len(level)-1):
                    level[i].next = level[i+1]
            
                level[-1].next = None
            
            level = next_level
        
        return root
        