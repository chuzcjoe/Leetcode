class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = collections.defaultdict(list)
        
        #print(sorted(tickets)[::-1])

        for fr,to in sorted(tickets)[::-1]:

            graph[fr].append(to)
        
        print(graph)
        res = []
        
        def dfs(start):
            while graph[start]:
                print(start)
                dfs(graph[start].pop())
            
            res.append(start)
        
        dfs("JFK")
        return res[::-1]
            
                
        