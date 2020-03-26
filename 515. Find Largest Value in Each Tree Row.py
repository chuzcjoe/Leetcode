# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        nodes = [root]
        MAXs = []
        
        if not root:
            return None
        else:
            MAXs.append(root.val)
        
        while nodes:
            nodes = [children for node in nodes for children in (node.left, node.right) if children]
            if not nodes:
                break
            MAXs.append(max([node.val for node in nodes]))
            
        return MAXs