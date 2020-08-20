class Solution:
    def threeEqualParts(self, A: List[int]) -> List[int]:
        
        n = A.count(1)
        if n == 0:
            return [0, len(A)-1]
        elif n % 3:
            return [-1,-1]
        
        target = []
        cnt = 0
        for a in A[::-1]:
            target.append(a)
            if a:
                cnt += 1
                if cnt == n//3:
                    break
        
        target = target[::-1]
        
        i = 0
        ans = []
        
        while i < len(A)-len(target):
            if A[i] and A[i:i+len(target)] == target:
                ans.append(i)
                i += len(target)
            elif A[i] == 0:
                i += 1
            else:
                return [-1,-1]
        
        return [ans[0]+len(target)-1, ans[1]+len(target)]
            
            
            
        