class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        #Input: n = 4, preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], pairs = [[0, 1], [2, 3]]
        ans = 0
        dic = collections.defaultdict(int)
        
        for m,n in pairs:
            dic[m] = n
            dic[n] = m
        
        def check(arr, x, v):
            for a in arr:
                if a == x:
                    return True
                elif a == v:
                    return False
                
            
        for x,y in pairs:
            if preferences[x][0] != y:
                i = 0
                while preferences[x][i] != y:
                    u = preferences[x][i]
                    v = dic[u]
                    flg = check(preferences[u], x, v)
                    if flg:
                        ans += 1
                        break
                    i += 1
            
            if preferences[y][0] != x:
                j = 0
                while preferences[y][j] != x:
                    u = preferences[y][j]
                    v = dic[u]
                    flg = check(preferences[u], y, v)
                    if flg:
                        ans += 1
                        break
                    j += 1
        
        return ans
                    
            
            