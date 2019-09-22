# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
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
            return 0
        
        dfs(root,array,'')
        #print(array)
        pth = [''.join(x[1:].split(',')) for x in array]
    
        pth = map(int,pth)
        #print(pth)
        
        return sum(pth)