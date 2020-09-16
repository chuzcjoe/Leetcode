"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return None
        
        queue = collections.deque([node])
        m = {node:Node(node.val)}
        
        while queue:
            size = len(queue)
            
            for _ in range(size):
                n = queue.popleft()
                value = n.val
                for nei in n.neighbors:
                    if nei not in m:
                        queue.append(nei)
                        m[nei] = Node(nei.val)
                    
                    m[n].neighbors.append(m[nei])
        
        return m[node]
                