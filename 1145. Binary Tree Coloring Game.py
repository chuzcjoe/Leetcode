# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        
        graph = collections.defaultdict(list)
        
        dummy = root
        def create_graph(root):
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
                create_graph(root.left)
                
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
                create_graph(root.right)
        
        create_graph(root)
 
        def dfs(node, seen):
            nonlocal res
            
            if node in seen:
                return
            
            res += 1
            seen.append(node)
            for i in graph[node]:
                dfs(i, seen[:])
        
        second_total = 0
        second = 0
        for i in graph[x]:
            res = 0
            dfs(i, [x])
            if second_total < res:
                second_total = res
                second = i

        
        return True if second_total > n //2 else False
        
       
        
                
        