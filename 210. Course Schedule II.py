class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        pres = collections.defaultdict(list)
        nxts = collections.defaultdict(list)
        for i, j in prerequisites:
            pres[i].append(j)
            nxts[j].append(i)
        
        all_course = [i for i in range(numCourses)]
        
        # queue stores the courses which have no prerequisites
        queue = collections.deque([i for i in all_course if i not in pres])
        count, res = 0, []

        while queue:
            start = queue.popleft()
            count += 1
            res.append(start)
            
            for nxt in nxts[start]:
                pres[nxt].remove(start)
                
                if not pres[nxt]:
                    queue.append(nxt)
                    
        if count == numCourses:
            return res
        else:
            return []
        
                
                
            
        