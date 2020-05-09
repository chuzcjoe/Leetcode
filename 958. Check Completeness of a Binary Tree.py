# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        
        """
        My solution
        
        if not root:
            return root
        
        def dfs(node, depth):
            nonlocal max_depth
            if not node:
                return
            
            max_depth = max(depth, max_depth)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        
        max_depth = -1
        dfs(root, 1)
        
        level = [root]
        depth = 0
        
        while level:
            depth += 1
            print(depth)
            if depth < max_depth and len(level) < 2**(depth-1):
                return False
            
            showed = False
            for node in level:
                for child in [node.left, node.right]:
                    if not child:
                        showed = True
                        continue
                    elif child and showed:
                        return False
                
            
            level = [child for node in level for child in [node.left, node.right] if child]
        
        return True
        """
        
        """
        DALAO solution
        """
        
        if not root:
            return root
        
        i = 0
        level = [root]
        
        while level[i]:
            level.append(level[i].left)
            level.append(level[i].right)
            i += 1
        
        if any(level[i:]):
            return False
        else:
            return True
        