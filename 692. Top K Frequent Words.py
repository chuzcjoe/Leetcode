class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        c = collections.Counter(words)
        
        res = []
        for s,v in c.items():
            res.append((v,s))
            
        
        res = sorted(res, key=lambda x: (-x[0],x[1]))
        
        return [s for _,s in res[:k]]
            