class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        res = [t%60 for t in time]
        
        dic = collections.defaultdict(int)
        cnt = 0
        
        for a in res:
            if a in dic:
                cnt += dic[a]
            
            if a == 0:
                dic[0] += 1
                
            dic[60-a] += 1
        
        return cnt