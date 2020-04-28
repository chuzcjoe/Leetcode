# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        
        dic = {}
        nums = [i for i in range(26)]
        alphas = [chr(i) for i in range(97,97+26)]
        
        for n,a in zip(nums,alphas):
            dic[n] = a
        
        if not root:
            return ""
        if not root.left and not root.right:
            return dic[root.val]
        
        def dfs(node, s):
            nonlocal res
            
            if not node.left and not node.right:
                s += dic[node.val]
                res = min(res, s[::-1])
                return
            
            s += dic[node.val]
            if node.left:
                dfs(node.left, s)
            if node.right:
                dfs(node.right, s)
        
        dummy = root
        res = 'z' * 8501
        dfs(root, '')
        
        return res