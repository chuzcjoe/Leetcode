# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        
        if not root:
            return []
        
        self.res = []
        
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            self.res.append(left+right+node.val)
            
            return left+right+node.val
        
        dfs(root)
        c = collections.Counter(self.res)
        s = sorted(c.items(), key = lambda x: x[1], reverse=True)
        most_freq = s[0][1]
        output = []
        for k,v in s:
            if v == most_freq:
                output.append(k)
            else:
                break
        
        return output
        