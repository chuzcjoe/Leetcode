# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        array = []
        
        def dfs(node,array,path):
            if not node:
                return
            if not node.left and not node.right:
                array.append(path+","+str(node.val))
                #print(array)
                return
            
            dfs(node.left,array,path+","+str(node.val))
            dfs(node.right,array,path+","+str(node.val))
        
        if not root:
            return []
        
        dfs(root,array,'')
        #print(array)
        pth = [x[1:].split(',') for x in array]
        pth = [map(int,x) for x in pth]
        
        results = [sum(x) for x in pth]
        return True if k in results else False