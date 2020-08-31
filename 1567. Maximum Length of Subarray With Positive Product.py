class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        
        """
        neg = [0]
        flag = 0
        for i,a in enumerate(nums):
            if a < 0:
                if flag:
                    flag = 0
                else:
                    flag = 1
                neg.append(flag)
            else:
                neg.append(flag)
        
        print(neg)
        
        first_zero, first_one = 0, None
        ans = 0
        
        for j in range(1, len(neg)):
            
            if nums[j-1] == 0:
                if neg[j] == 1:
                    first_one = j
                    first_zero = None
                else:
                    first_one = None
                    first_zero = j
                continue
                
            elif neg[j] == 0 and first_zero is None:
                first_zero = j
            elif neg[j] == 1 and first_one is None:
                first_one = j
            
            if neg[j] and first_one is not None and first_one != j:
                ans = max(ans, j-first_one)
            elif neg[j] == 0 and first_zero is not None:
                ans = max(1, ans, j-first_zero)
        
        return ans
        """
        
        n = len(nums)
        pos = [0] * n
        neg = [0] * n
        
        
        if nums[0] > 0:
            pos[0] = 1
        elif nums[0] < 0:
            neg[0] = 1
        ans = pos[0]
        
        for i,a in enumerate(nums[1:], 1):
            if a > 0:
                pos[i] = pos[i-1] + 1
                neg[i] = neg[i-1] + 1 if neg[i-1] > 0 else 0
            elif a < 0:
                pos[i] = neg[i-1] + 1 if neg[i-1] > 0 else 0
                neg[i] = pos[i-1] + 1
            
            print(pos[i])
            ans = max(ans, pos[i])
        
        return ans
                
            
            
            