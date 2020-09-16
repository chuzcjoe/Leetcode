# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        """
        1. inorder then build tree
        
        vals = []
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            vals.append(root.val)
            inorder(root.right)
        
        inorder(root)
        
        bisect.insort_left(vals, val)
        
        def build(vals,l,r):
            if l > r:
                return
            
            mid = (l+r) // 2
            
            root = TreeNode(vals[mid])
            
            root.left = build(vals,l,mid-1)
            root.right = build(vals,mid+1,r)
            
            return root
        
        return build(vals, 0, len(vals)-1)
        """
        
        def insert(root):
            if not root:
                return TreeNode(val)
            
            if val > root.val:
                root.right = insert(root.right)
            elif val < root.val:
                root.left = insert(root.left)
            
            return root
        
        return insert(root)
        
            
        
        
        