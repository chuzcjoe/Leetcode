# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        
        
        if not root:
            return root
        
        res = []
        level = [root]
        
        while level:
            
            tmp = []
            for node in level:
                tmp += [node.val]
            res.append(tmp)
            level = [child for node in level for child in [node.left, node.right] if child]
        
        return res[::-1]