class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        circle = [i for i in range(len(M))]
        
        cnt = 0
        
        def dfs(x,M,f,visited):
            for i in range(0,len(M)):
                if M[x][i] == 1 and i not in visited:
                    f.append(i)
                    visited.add(i)
                    dfs(i,M,f,visited)
            
        
        while circle:
            start = circle[0]
            cnt += 1
            frds = []
            frds.append(start)
            dfs(start,M,frds,{start})
            print(circle)
            for std in frds:
                circle.remove(std)
        
        
        return cnt