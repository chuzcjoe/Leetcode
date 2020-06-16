class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        
        """
        self.graph = collections.defaultdict(int)
        for cur,par in enumerate(parent):
            self.graph[cur] = par
        """
        
        m = 1 + int(math.log2(n)) # levels
        self.dp = [[-1]*m for _ in range(n)] # node i's 2^j parent
        
        for j in range(m):
            for i in range(n):
                if j == 0:
                    self.dp[i][j] = parent[i]
                elif self.dp[i][j-1] != -1:
                    self.dp[i][j] = self.dp[self.dp[i][j-1]][j-1]

    def getKthAncestor(self, node: int, k: int) -> int:
        
        """
        visited = []
        ans = -1
        
        #dfs
        def dfs(node, cnt):
            nonlocal ans
    
            if node == -1:
                return
            
            if cnt == k:
                ans = node
                return
            
            dfs(self.graph[node], cnt+1)
        
        dfs(node, 0)
        
        
        if ans == -1:
            return -1
        else:
            return ans
        """
        
        while k > 0 and node != -1:
            i = int(math.log2(k))
            node = self.dp[node][i]
            k -= (1<<i)
        
        return node
        
        
        


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)