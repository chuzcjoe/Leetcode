# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node, parent, grand):
            if not node: # base case
                return
            
            nonlocal SUM 
            if parent and grand and grand.val % 2 == 0:
                SUM += node.val
            
            dfs(node.left,node,parent)
            dfs(node.right,node,parent)
        
        SUM = 0
        dfs(root, None, None)
        return SUM
        
    
        
        """
        if not root:
            return 
        
        if root.val % 2 == 0:
            cnt = 0
            cur = [root]
            while cnt < 2:
                pre, cur = cur, [child for q in cur for child in [q.left, q.right] if child]
                cnt += 1
            while cur:
                nodes.append(cur.pop())
        
        self.sumEvenGrandparent(root.left, nodes)
        self.sumEvenGrandparent(root.right, nodes)
        print([node.val for node in nodes])
        
        return sum([node.val for node in nodes])""
        """