"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        if not head:
            return None
        
        queue = collections.deque([head])
        m = {head: Node(head.val)}
        
        while queue:
            size = len(queue)
            
            for _ in range(size):
                n = queue.popleft()
                
                nxt = n.next
                rand = n.random
                
                if nxt and nxt not in m:
                    m[nxt] = Node(nxt.val, nxt.next, nxt.random)
                    queue.append(nxt)
                
                if rand and rand not in m:
                    m[rand] = Node(rand.val, rand.next, rand.random)
                    queue.append(rand)
                
                m[n].next = m[nxt] if nxt else None
                m[n].random = m[rand] if rand else None
        
        return m[head]