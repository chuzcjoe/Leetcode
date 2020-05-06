# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        
        """
        1.DFS solution
        
        def find(node, target):
            nonlocal cnt
            
            if not node:
                return
            
            if node.val == target:
                cnt += 1
            
            find(node.left, target-node.val)
            find(node.right, target-node.val)
        
        def dfs(node, target):
            if not node:
                return
            
            find(node, target)
            dfs(node.left, target)
            dfs(node.right, target)
        
        cnt = 0
        dfs(root, sum)
        
        return cnt
        """
        
        
        """
        2. Hashmap solution O(N)
        """
        path = collections.defaultdict(int)
        path[0] = 1
        
        def dfs(node, presum, target):
            nonlocal cnt
            if not node:
                return
            
            cur_sum = presum + node.val
            if cur_sum-target in path:
                cnt += path[cur_sum-target]
            
            path[cur_sum] += 1
            
            dfs(node.left, cur_sum, target)
            dfs(node.right, cur_sum, target)
            
            #This is the key, when we switch to a new branch, we need to remove 1 from the previous branch
            path[cur_sum] -= 1
        
        cnt = 0
        dfs(root, 0, sum)
        return cnt
            
            