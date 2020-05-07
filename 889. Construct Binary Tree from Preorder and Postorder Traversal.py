# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        
        #by looking at the pre and pose, we can see that if 1 in pre is the root,
        #then pre[1] is the left node of 1 and post[-2] is the right node of 1
        #so we can recursively find subset of pre and post to construct a tree
        
        def buildTree(pre, post):
            
            if not pre or not post:
                return None
            
            root = TreeNode(pre[0])
            if len(post) == 1:
                return root
            
            i = pre.index(post[-2])
            root.left = buildTree(pre[1:i],post[:i-1])
            root.right = buildTree(pre[i:],post[i-1:-1])
            
            return root
        
        return buildTree(pre, post)
            
            
            
        