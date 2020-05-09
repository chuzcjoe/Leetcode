# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        
        graph = collections.defaultdict(list)
        
        def buildGraph(node):
            if not node:
                return
            
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
            
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
            
            buildGraph(node.left)
            buildGraph(node.right)
        
        buildGraph(root)
        
        def find(node, prev, d):
            nonlocal res
            if d == K:
                res.append(node.val)
                return
            
            for nei in graph[node]:
                if nei != prev:
                    find(nei, node, d+1)
                    
        
        def dfs(node):
            
            if not node:
                return
            if node.val == target.val:
                find(node, None, 0)
            
            dfs(node.left)
            dfs(node.right)
            
        res = []
        
        dfs(root)
        
        return res