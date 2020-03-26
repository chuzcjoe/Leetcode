# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        
        children = [root]
        left_most = root.val
        
        while children:
            left_children = [child.left for child in children if child.left]
            right_children = [child.right for child in children if child.right]
            children = left_children + right_children
            if not children:
                break
            left_most = children[0].val
        
        return left_most