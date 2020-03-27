class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        
        count = 1
        
        def if_unique(s):
            return len(s) == len(set(s))
        
        nums1 = [str(i) for i in range(10)]
        nums2 = [str(i) for i in range(1,10)]
        
        def backtrack(path, nums1, nums2):
            nonlocal count
            
            nums = nums2 if not path else nums1
            
            if path and len(path) > n:
                return
            
            if path:
                if if_unique(path):
                    count += 1
                else:
                    return
            
            
            for num in nums:
                if num in path: # this is the tricky part, reduce backtracking steps greatly!
                    continue
                else:
                    path += num
                backtrack(path, nums1, nums2)
                path = path[:-1]
        
        backtrack("", nums1, nums2)
        return count
                
            
            