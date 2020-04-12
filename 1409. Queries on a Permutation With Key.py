class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = [i+1 for i in range(m)]
        res = []
        for i in range(len(queries)):
            pos = P.index(queries[i])
            res.append(pos)
            val = P.pop(pos)
            P.insert(0, val)
        
        return res