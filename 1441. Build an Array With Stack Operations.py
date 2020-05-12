class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        res = []
        for i in range(1,n+1):
            if i in target:
                res.append('Push')
                if target.index(i)+1 == len(target):
                    break
            else:
                res.append("Push")
                res.append("Pop")
        
        return res
        