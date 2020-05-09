# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        def preorder(node):
            if not node:
                self.res.append('#')
                return
            
            self.res.append(node.val)
            preorder(node.left)
            preorder(node.right)
        
        self.res = []
        preorder(root)
        return self.res
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        def dfs(data):
            
            val = data.pop(0)
            if val == '#':
                return None
            
            root = TreeNode(val)
            root.left = dfs(data)
            root.right = dfs(data)
            
            return root
        
        return dfs(data)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))