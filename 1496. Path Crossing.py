class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        dic = {'N':[-1,0],'S':[1,0],'E':[0,1],'W':[0,-1]}
        visited = {(0,0)}
        x = y = 0
        
        for p in path:
            nx, ny = dic[p]
            x = x + nx
            y = y+ny
            if (x,y) in visited:
                return True
            else:
                visited.add((x,y))
        
        return False
            