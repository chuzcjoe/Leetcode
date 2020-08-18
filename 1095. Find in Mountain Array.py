# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        n = mountain_arr.length()
        
        l, r = 0, n-1
        #find top
        while l < r:
            mid = l + (r-l)//2
            
            cur_v = mountain_arr.get(mid)
            next_v = mountain_arr.get(mid+1)
            
            if cur_v < next_v:
                l = mid + 1
            else:
                r = mid
        
        top = l
        
        l, r = 0, top
        
        while l <= r:
            mid = r - (r-l) // 2
            
            v = mountain_arr.get(mid)
            if v == target:
                return mid
            elif v > target:
                r = mid - 1
            else:
                l = mid + 1
        
        l, r = top, n-1
        
        while l <= r:
            mid = r - (r-l) // 2
            
            v = mountain_arr.get(mid)
            if v == target:
                return mid
            elif v > target:
                l = mid +1
            else:
                r = mid -1
        
        
        return -1