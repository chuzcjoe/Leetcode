# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        
        """
        Solution 1:
        
        vals = []
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)
        
        inorder(root)
        
        for i,x in enumerate(vals):
            if x == key:
                vals.pop(i)
        
        def buildTree(vals, i, j):
            if i > j :
                return
            
            mid = (i+j) // 2
            root = TreeNode(vals[mid])
            root.left = buildTree(vals, i, mid-1)
            root.right = buildTree(vals, mid+1, j)
            
            return root
        
        return buildTree(vals,0,len(vals)-1)
        """
        
        """
        Solution 2: one pass
        """
        
        def dfs(node, key):
            if not node:
                return
            
            if node.val > key:
                node.left = dfs(node.left, key)
            elif node.val < key:
                node.right = dfs(node.right, key)
            else:
                if not node.left:
                    return node.right
                
                else:
                    tmp = node.left
                    while tmp.right:
                        tmp = tmp.right
                    
                    node.val = tmp.val
                    
                    node.left = dfs(node.left, tmp.val)
            
            return node
        
        return dfs(root, key)
                
                
                
        
            
            
            
            