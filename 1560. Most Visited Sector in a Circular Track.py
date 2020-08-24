class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        
        ans = collections.Counter()
        
        for i in range(len(rounds)-1):
            s = rounds[i]
            e = rounds[i+1]
            
            if s < e:
                c = collections.Counter([x for x in range(s,e)])
            else:
                c = collections.Counter([x for x in range(s,n+1)]+[y for y in range(1,e)])
            
            ans.update(c)
        
        ans[rounds[-1]] += 1
        
        ans = sorted(ans.items(), key=lambda x: x[1], reverse=True)
        
        freq = ans[0][1]
        
        res = []
        for a,b in ans:
            if b != freq:
                break
            
            res.append(a)
        
        return sorted(res)