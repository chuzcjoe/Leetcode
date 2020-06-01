class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        #horizontal cut determines the height of each piece
        #vertical cut determines the width of each piece
        horizontalCuts = sorted(horizontalCuts)
        horizontalCuts.append(h)
        verticalCuts = sorted(verticalCuts)
        verticalCuts.append(w)
        
        #h cuts
        hs = []
        for i,h in enumerate(horizontalCuts):
            if i == 0:
                hs.append(h)
            else:
                hs.append(horizontalCuts[i]-horizontalCuts[i-1])
        
        
        #v cuts
        vs = []
        for i,h in enumerate(verticalCuts):
            if i == 0:
                vs.append(h)
            else:
                vs.append(verticalCuts[i]-verticalCuts[i-1])
        
        return max(hs)*max(vs) % (10**9+7)
            
        