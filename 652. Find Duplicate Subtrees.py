# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        
        """
        solution1: serialize O(n^2)
        def serialize(node):
            nonlocal res
            
            if not node:
                res.append('#')
                return
            
            res.append(str(node.val))
            serialize(node.left)
            serialize(node.right)
            
        def decode(data):
            val = data.pop(0)
            
            if val == '#':
                return None
            
            root = TreeNode(int(val))
            root.left = decode(data)
            root.right = decode(data)
            
            return root
            
        
        table = collections.defaultdict(int)
        
        def find(node):
            nonlocal nodes, res
            if not node:
                return
            
            res = []
            serialize(node)
            if table[",".join(res)]>=1:
                nodes.append(",".join(res))
            
            table[",".join(res)] += 1
                
            
            find(node.left)
            find(node.right)
            
        res = [] 
        nodes = []
        find(root)
        output = []
        nodes = list(set(nodes))
        for node in nodes:
            output.append(decode(node.split(',')))
        return output
        
        """
        
        
    
        
        """
        Solution 2, refine of solution 1
        
        
        """
        def serialize(node, ans, table):
            if not node:
                return '#'
            
            key = str(node.val) + ',' + serialize(node.left, ans, table) + ',' + serialize(node.right, ans, table)
            
            table[key] += 1
            if table[key] == 2:
                ans.append(node)
            
            return key
        
        ans = []
        table = collections.defaultdict(int)
        serialize(root, ans, table)
        
        return ans
    
        
        
    
    