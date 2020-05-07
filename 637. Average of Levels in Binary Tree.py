# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        
        if not root:
            return 0
        
        level = [root]
        res = []
        
        while level:
            
            nodes = [node.val for node in level]
            res.append(sum(nodes)/len(nodes))
            
            level = [child for node in level for child in [node.left, node.right] if child]
        
        return res
            
            
        