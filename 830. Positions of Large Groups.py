class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        
        res = []
        start = 0
        
        for i,s in enumerate(S):
            if i == len(S)-1:
                if i-start+1 >= 3:
                    res.append([start,i])
                break
                
            if S[i] != S[i+1]:
                if i-start+1 >= 3:
                    res.append([start,i])
                
                start = i+1
        
        return res
            