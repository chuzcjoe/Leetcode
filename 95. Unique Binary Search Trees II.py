# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        if n == 0:
            return []
        
        def build(first, last):
            
            trees = []
            for root in range(first, last+1):
                for left in build(first, root-1):
                    for right in build(root+1, last):
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        trees.append(node)
            
            return trees or [None]
        
        return build(1,n)
            