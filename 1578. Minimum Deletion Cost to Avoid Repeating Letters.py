class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        
        itvs = []
        left, right = 0, 0
        ans = 0
        
        while right < len(s):
            
            while right < len(s) and s[left] == s[right]:
                right += 1
            
            if right-left >= 2:
                itvs.append([left,right-1])
            left = right
        print(itvs)
        for itv in itvs:
            tmp = sorted(cost[itv[0]:itv[1]+1])
            ans += sum(tmp[:itv[1]-itv[0]])
        
        return ans
            
                