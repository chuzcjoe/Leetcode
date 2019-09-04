class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        
        
        nums = [int(x) for x in range(1,n+1)]
        
        def permute(m):
            temp = 1
            for i in range(1,m+1):
                temp *= i
            return temp
        
        res = []
        
        
        def dfs(nums,res,k):
            if len(res) == n:
                return 
            
            idx = (k-1) / permute(len(nums)-1)
            res.append(nums[idx])
            nums.pop(idx)
            #print(res)
            #print(nums)
            dfs(nums,res,k-idx*permute(len(nums)))
        
        dfs(nums,res,k)
        
        return "".join([str(x) for x in res])
            
        
        
        