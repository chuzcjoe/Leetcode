class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        n = len(rating)
        
        def form(soldiers):
            if soldiers[0] > soldiers[1] > soldiers[2] or soldiers[0] < soldiers[1] < soldiers[2]:
                return True
            else:
                return False
            
        def backtrack(team, option):
            
            nonlocal count
            
            
            if len(team) == 3:
                if form(team):
                    count += 1
                    return
            
            for i in range(len(option)):
                if len(team) == 3:
                    return
                else:
                    team.append(option[i])
                    backtrack(team[:], option[i+1:])
                    team.pop(-1)
        
        team = []
        count = 0
        
        backtrack(team, rating)
        return count
                
            
        