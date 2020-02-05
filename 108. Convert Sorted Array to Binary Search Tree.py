# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        root = TreeNode(0)
        
        def dfs(nums):
            if not nums:
                return
            
            mid = len(nums) // 2
            
            root = TreeNode(nums[mid])
            root.left = dfs(nums[:mid])
            root.right = dfs(nums[mid+1:])
            
            return root
        
        root = dfs(nums)
        
        return root
            
            
            
        