class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        
        stack = []
        ans = []
        
        index = 0
        
        while index < len(T):
            
            ans.append(0)
            cur_T = T[index]
            
            while stack and stack[-1][0] < cur_T:
                last = stack.pop()
                ans[last[1]] = index - last[1]
            
            stack.append((cur_T, index))
            index += 1
        
        return ans