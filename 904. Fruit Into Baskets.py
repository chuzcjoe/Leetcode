class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        
        n = len(tree)
        left = 0
        res = 0
        
        
        cur = collections.deque()
        counter = collections.Counter()
        
        for right in range(n):
                counter[tree[right]] += 1
                
                while len(counter) > 2:
                    counter[tree[left]] -= 1
                    if counter[tree[left]] == 0:
                        counter.pop(tree[left])
                    left += 1
                
                
                res = max(res, right-left+1)
                
        return res
        
        
    
                
        
            
        