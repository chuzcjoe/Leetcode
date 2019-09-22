# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        array = []
        
        def dfs(node,array,path):
            if not node:
                return
            if not node.left and not node.right:
                array.append(path+"->"+str(node.val))
                #print(array)
                return
            
            dfs(node.left,array,path+"->"+str(node.val))
            dfs(node.right,array,path+"->"+str(node.val))
        
        if not root:
            return []
        
        dfs(root,array,"")
        
        return [x[2:] for x in array]