class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        
        graph = collections.defaultdict(list)
        res = collections.defaultdict()
        vals = collections.defaultdict()
        
        for i, eq in enumerate(equations):
            graph[eq[0]].append(eq[1])
            graph[eq[1]].append(eq[0])
            res[eq[0]+'/'+eq[1]] = values[i]
            
        print(res)
        while equations:
            cur_node = equations[0][1]
                
            for nxt in graph[cur_node]:
                    if cur_node not in vals and nxt not in vals:
                        if cur_node+'/'+nxt in res:
                            vals[nxt] = 1.0
                            vals[cur_mode] = 1.0 * res[cur_node+'/'+nxt]
                            equations.remove([cur_node, nxt])
                        else:
                            vals[cur_node] = 1.0
                            vals[nxt] = 1.0 * res[nxt+'/'+cur_node]
                            equations.remove([nxt, cur_node])
                            
                    elif cur_node+'/'+nxt in res:
                        if cur_node in vals:
                            vals[nxt] = vals[cur_node] / res[cur_node+'/'+nxt]
                        else:
                            vals[cur_node] = vals[nxt] * res[cur_node+'/'+nxt]
                        equations.remove([cur_node, nxt])
                        
                    elif nxt+'/'+cur_node in res:
                        if cur_node in vals:
                            vals[nxt] = vals[cur_node] * res[nxt+'/'+cur_node]
                        else:
                            vals[cur_node] = vals[nxt] / res[nxt+'/'+cur_node]
                        equations.remove([nxt,cur_node])
                        
                
                
        
        out = []
        for x,y in queries:
            if x in vals and y in vals:
                out.append(vals[x]/vals[y])
            else:
                out.append(-1.0)
        
        return out