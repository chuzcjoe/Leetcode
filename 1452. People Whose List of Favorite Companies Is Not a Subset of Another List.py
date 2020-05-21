class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        
        n = len(favoriteCompanies)
        Companies = []
        res = [k for k in range(n)]
        for c in favoriteCompanies:
            Companies.append(set(c))
        
        for i in range(n):
            for j in range(n):
                if i != j:
                    if len(Companies[i]) <= len(Companies[j]) and not(Companies[i]-Companies[j]):
                        res.remove(i)
                        break
        
        return res
                    
                    