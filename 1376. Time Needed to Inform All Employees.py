class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        # dp solution: up to bottom
        # time: max(manager's employees) + informtime(manager)
        
        # sub-array: ith manager's employees
        children = [[] for i in range(n)]
        
        for i,m in enumerate(manager):
            if m >= 0:
                children[m].append(i)
        
        def dfs(i):
            return max([dfs(j) for j in children[i]] or [0]) + informTime[i]
        
        return dfs(headID)