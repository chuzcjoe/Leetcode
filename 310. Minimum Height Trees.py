class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if not edges:
            return [0]
        
        path = collections.defaultdict(list)
        leaves = []
        for x,y in edges:
            path[x].append(y)
            path[y].append(x)
        
        for k,v in path.items():
            if len(v) == 1:
                leaves.append(k)
        
            
        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for lf in leaves:
                nxt = path[lf].pop()
                path[nxt].remove(lf)
                
                if len(path[nxt]) == 1:
                    newLeaves.append(nxt)
            
            leaves = newLeaves[:]
        
        return leaves
            
        
            
        
            
                    
            
            
        