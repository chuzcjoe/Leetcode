# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        
        def check(nums):
            c = collections.Counter(nums)
            #odd length
            if len(nums)&1:
                if sum(v&1 for v in c.values()) == 1:
                    return True
                else:
                    return False
            
            else:
                if all(v&1==0 for v in c.values()):
                    return True
                else:
                    False
        
        def dfs(node, path):
            nonlocal res
            
            if not node:
                return
            
            if not node.left and not node.right:
                if check(path+[node.val]):
                    res += 1
                
                return
            
            path.append(node.val)
            
            dfs(node.left, path[:])
            dfs(node.right, path[:])
        
        res = 0
        dfs(root, [])
        
        return res
            
                
        