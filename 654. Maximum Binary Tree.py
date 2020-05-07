# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        
        def buildTree(nums,i,j):
            if i >= j:
                return
            
            maxi = max(nums[i:j])
            idx = nums.index(maxi)
            
            root = TreeNode(maxi)
            root.left = buildTree(nums,i,idx)
            root.right = buildTree(nums,idx+1,j)
            
            return root
        
        return buildTree(nums,0,len(nums))
            