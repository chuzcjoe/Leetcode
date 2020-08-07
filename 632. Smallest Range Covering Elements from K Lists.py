class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        
        """
        #1. Heap
        
        q = [(num[0], i, 0) for i,num in enumerate(nums)]
        heapq.heapify(q)
        left = -1e5
        right = 1e5
        
        MIN = -1e5
        MAX = max(num[0] for num in nums)
        
        while q:
            a, i, j = heapq.heappop(q)
            MIN = a
            
            if MAX - MIN < right - left:
                right = MAX
                left = MIN
            
            if j == len(nums[i])-1:
                return [left, right]
            
            MAX = max(nums[i][j+1], MAX)
            heapq.heappush(q, (nums[i][j+1], i, j+1))
        """
        
        #2. sliding window
        d = []
        n = len(nums)
        ans = -1e5, 1e5
        
        for i,num in enumerate(nums):
            for a in num:
                d.append([a, i])
        
        d = sorted(d, key=lambda x: x[0])
        left = 0
        k = collections.defaultdict(int)
        print(d)
        
        for right,x in enumerate(d):
            k[x[1]] += 1
            
            while len(k.keys()) == n:
                if x[0]-d[left][0] < ans[1] - ans[0]:
                    ans = d[left][0], x[0] 
                    
                val = d[left][1]
                k[val] -= 1
                if k[val] == 0:
                    del k[val]
                    
                left += 1
        
        return ans
            
            
            
            
            
            
            