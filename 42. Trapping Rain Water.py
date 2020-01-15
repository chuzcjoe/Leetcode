class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # from left to right, fill up water
        l_to_r = copy.deepcopy(height)
        for i in range(0,len(height)-1):
            if l_to_r[i+1] < l_to_r[i]:
                l_to_r[i+1] = l_to_r[i]
            
        # from right to right, fill up water
        r_to_l = copy.deepcopy(height)
        for i in range(len(height)-1,0,-1):
            if r_to_l[i-1] < r_to_l[i]:
                r_to_l[i-1] = r_to_l[i]
            
        ans = 0    
        for i in range(len(height)):
            ans += min(l_to_r[i], r_to_l[i]) - height[i]
        
        return ans