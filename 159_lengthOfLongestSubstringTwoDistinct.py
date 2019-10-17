def lengthOfLongestSubstringTwoDistinct(s):
    
    length = []
    start = 0
    end = 0
    visited = []
    
    def same_char(s):
        c = s[0]
        for x in s:
            if x != c:
                return False
            
        return True
    
    for i,x in enumerate(s):
        if len(visited) < 2:
            if x not in visited:
                visited.append(x)
                end = i
            else:
                end = i
        
        if len(visited) == 2:
            if x in visited:
                if i == len(s)-1:
                    length.append(i-start+1)
                else:
                    end = i
            else:
                end = i
                
                length.append(end-start)
                
                c1 = visited[0]
                c2 = visited[1]
                while not same_char(s[start:end]):
                    start += 1
                if s[start] == c1:
                    visited.pop(1)
                else:
                    visited.pop(0)
                visited.append(x)
                print(visited)
                

                
                    
   
    return max(length)