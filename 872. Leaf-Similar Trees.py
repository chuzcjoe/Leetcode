# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        
        def dfs(root,seq):
            if not root:
                return 
            if not root.left and not root.right:
                seq.append(root.val)
                return
                
            dfs(root.left,seq)
            dfs(root.right,seq)
        
        seq1 = []
        seq2 = []
        
        dfs(root1,seq1)
        dfs(root2,seq2)
        
        return seq1 == seq2