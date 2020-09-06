class Solution:
    def numWays(self, s: str) -> int:
        
        cnt = collections.Counter(s)
        ans = 0
        
        if cnt['1'] % 3:
            return 0
        elif cnt['1'] == 0:
            return math.comb(len(s)-1, 2) % (10**9+7)
        
        n = cnt['1'] // 3
        
        #from the end, find # of leading zeros
        lz_cnt = 0
        o_cnt = 0
        for i,a in enumerate(s[::-1]):
            if a == '1' and o_cnt < n:
                o_cnt += 1
            elif a == '1' and o_cnt == n:
                break
            elif a == '0' and o_cnt == n:
                lz_cnt += 1
        
        #from the start, find # of ending zeros
        ez_cnt = 0
        o_cnt = 0
        for j, b in enumerate(s):
            if b == '1' and o_cnt < n:
                o_cnt += 1
            elif b == '1' and o_cnt == n:
                break
            elif b == '0' and o_cnt == n:
                ez_cnt += 1
        
        return (lz_cnt+1)*(ez_cnt+1) % (10**9+7)
        
                
        
        
        
        