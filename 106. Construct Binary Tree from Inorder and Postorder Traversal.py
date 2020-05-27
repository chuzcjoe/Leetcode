# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        #observe: if 3 in post is the root, then post[-2] is the right node,
        #inorder[0] is the left node
        
        def build(inorder, postorder):
            
            if not inorder or not postorder:
                return None
            
            root = TreeNode(postorder[-1])
            if len(postorder) == 1:
                return root
            
            j = inorder.index(postorder[-1]) #find root node index in inorder
            
            
            root.left =  build(inorder[:j], postorder[:j])
            root.right = build(inorder[j+1:], postorder[j:-1])
            
            return root
        
        return build(inorder, postorder)