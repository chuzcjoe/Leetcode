# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        
        """
        My solution(TLE) (107/108)
        
         if not root:
            return 0
        
        level = [root]
        res = 0
        
        def cal_width(nodes):
            left = 0
            right = len(nodes)-1
            
            while left < len(nodes):
                if nodes[left]:
                    break
                
                left += 1
            
            while right >= 0:
                if nodes[right]:
                    break
                
                right -= 1
            
            return left, right
        
        while any(level):
            
            l,r = cal_width(level)
            res = max(res, r-l+1)
            
            new_level = []
            for node in level:
                if node:
                    new_level.append(node.left)
                    new_level.append(node.right)
                else:
                    new_level.extend([None, None])
            
            level = new_level
                
        
        return res
        """
        #tree numbering
        #          1
        #  2                3
        #4  5             6   7
        
        width = 0
        level = [(1, root)]
        while level:
            width = max(width, level[-1][0] - level[0][0] + 1)
            level = [kid
                 for number, node in level
                 for kid in enumerate((node.left, node.right), start=2 * number)
                 if kid[1]]
        return width
       
    
        