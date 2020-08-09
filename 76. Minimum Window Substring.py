class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        """
        first version
        
        t = collections.Counter(t)
        ans = ""
        seen = collections.defaultdict(int)
        left = 0
        flag = False

        for right,a in enumerate(s):
            flag = False
            seen[a] += 1
            
            while all(seen[x]>=t[x] for x in t):
                flag = True
                seen[s[left]] -= 1
                left += 1
            
            if flag:
                seen[s[left-1]] += 1
                left -= 1
                if not ans:
                    ans = s[left:right+1]
                elif len(ans) > right-left+1:
                    ans = s[left:right+1]

        return ans
        """
        
        #modified
        found = 0
        target = collections.Counter(t)
        ans = ""
        
        left = 0
        
        for right,a in enumerate(s):
            if target[a] > 0:
                found += 1
            target[a] -= 1
            
            while found == len(t):
                if not ans or len(ans) > right-left+1:
                    ans = s[left:right+1]
                
                target[s[left]] += 1
                if target[s[left]] > 0:
                    found -= 1
                    
                left += 1
        
        return ans
            
        