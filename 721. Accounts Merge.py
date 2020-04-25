class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        acc_map = collections.defaultdict(list)
        visited = [0] * len(accounts)
        
        for i, account in enumerate(accounts):
            for acc in account[1:]:
                acc_map[acc].append(i)
        
        def dfs(i, emails):
            if visited[i]:
                return
            
            visited[i] = 1
            
            for email in accounts[i][1:]:
                emails.add(email)
                
                for neighbor in acc_map[email]:
                    dfs(neighbor, emails)

        
        res = []
        
        for i, account in enumerate(accounts):
            if visited[i]:
                continue
                
            name, emails = account[0], set()
            
            dfs(i, emails)
            res.append([name]+sorted(emails))
        
        return res
            
            
            
            
            
        
        