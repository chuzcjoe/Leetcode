# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        
        def dfs(preorder):
            if not preorder:
                return
            
            val = preorder.pop(0)
            root = TreeNode(val)

            idx = len(preorder)
            for i,num in enumerate(preorder):
                if num > val:
                    idx = i
                    break

            root.left = dfs(preorder[0:idx])
            root.right = dfs(preorder[idx:])
        
            return root
        
        return dfs(preorder)