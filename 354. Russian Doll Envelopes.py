class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        
        #O(nlogn) solution with binary search
        n = len(envelopes)
        if not envelopes:
            return 0
        
        def f(x,y):
            return -1 if x[0] < y[0] or x[0]==y[0] and x[1] > y[1] else 1
        
        envelopes.sort(cmp=f)
        print(envelopes)
        
        env = [x[1] for x in envelopes]
        
        def binarySearch(array,val):
            lo, hi = 0, len(array)-1
            while(lo <= hi):
                mid = (lo+hi) // 2
                if array[mid] > val:
                    hi = hi - 1
                elif array[mid] < val:
                    lo = lo + 1
                else:
                    return mid
            return lo
        
        results = []
        
        for val in env:
            pos = binarySearch(results,val)
            
            if pos == len(results):
                results.append(val)
            else:
                results[pos] = val
                
        return len(results)
        