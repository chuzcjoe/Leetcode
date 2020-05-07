# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        def convert2(nums):
            res = 0
            for i,x in enumerate(nums[::-1]):
                res += x*2**(i)
            return res
        
        def dfs(node, path):
            nonlocal sum
            
            #we reach the leaves.
            if not node.left and not node.right:
                sum += convert2(path+[node.val])
                return
            #cases where we did not reach the leaves nodes.
            path.append(node.val)
            if node.left:
                dfs(node.left, path[:])
            if node.right:
                dfs(node.right, path[:])
        
        sum = 0
        dfs(root, [])
        return sum