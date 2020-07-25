class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        graph = collections.defaultdict(list)
        ans = []
        
        for i,j in pairs:
            graph[i].append(j)
            graph[j].append(i)
        
        f = {}
        def find(x):
            f.setdefault(x,x)
            if x != f[x]:
                f[x] = find(f[x])
            
            return f[x]
        
        def union(x,y):
            f[find(x)] = find(y)
        
        for x,y in pairs:
            union(x,y)
        
        cluster = collections.defaultdict(list)
        for i in range(len(s)):
            cluster[find(i)].append(s[i])
            
        for c in cluster.keys():
            cluster[c].sort(reverse=True)
        
        for j in range(len(s)):
            ans.append(cluster[find(j)].pop())
        
        return "".join(ans)