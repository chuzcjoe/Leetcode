class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], label: str) -> List[int]:
        
        graph = collections.defaultdict(list)
        
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        def dfs(node, parent):
            counter = collections.Counter()
            
            for child in graph[node]:
                if child == parent:
                    continue
                
                counter += dfs(child, node)
            
            counter[label[node]] += 1
            ans[node] = counter[label[node]]
            
            return counter
        
        ans = [0] * n
        dfs(0, None)
        
        return ans