class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        max_len = 0
        
        def is_unique(path):
            return len("".join(path)) == len(set("".join(path)))
        
        def backtrack(path, start, option):
            
            nonlocal max_len
            
            if path and is_unique(path):
                max_len = max(len("".join(path)), max_len)
            
            
            for i in range(start, len(option)):
                path.append(option[i])
                backtrack(path, i+1, option)
                path.pop(-1)
                
        
        backtrack([], 0, arr)
        return max_len
                
        