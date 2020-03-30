class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        n = len(tiles)
        cnt = 0
        
        def backtrack(path, option, n, seen):
            
            nonlocal cnt
            
            if len(path) < 0 or len(path) > n:
                return
            else:
                if path not in seen and path:
                    seen.add(path)
                    print(path)
                    cnt += 1
            
            for i in range(len(option)):
                add = option.pop(i)
                path += add 
                backtrack(path, option, n, seen)
                option.insert(i,add)
                path = path[:-1]
        
        opt = [x for x in tiles]
        seen = set()
        backtrack("", opt, n, seen)
        
        return cnt