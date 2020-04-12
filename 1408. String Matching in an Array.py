class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        
        for i,w in enumerate(words):
            for s in words[:i]+words[i+1:]:
                if w in s:
                    res.append(w)
        return set(res)