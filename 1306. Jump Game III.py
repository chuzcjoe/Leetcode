class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        queue = collections.deque([start])
        visited = set()
        visited.add(start)
        
        while queue:
            x = queue.popleft()
            
            for jump in [-arr[x], arr[x]]:
                if 0 <= jump + x < len(arr):
                    if arr[jump+x] == 0:
                        return True
                    if jump+x in visited:
                        continue
                        
                    queue.append(jump+x)
                    visited.add(jump+x)
        
        return False
                    
            
            