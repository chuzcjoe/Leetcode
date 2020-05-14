class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        
        S = sum(A)
        
        if S % 3:
            return False
        
        sub = S // 3
        res = 0
        cnt = 0
        
        for i in A:
            res += i
            
            if res == sub:
                cnt += 1
                res = 0
        
        if cnt == 3:
            return True
        elif cnt > 3 and sub == 0:
            return True
        else:
            return False