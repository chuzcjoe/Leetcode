class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        
        def kSmallestPairs(nums1, nums2, k=200):
            if not(nums1 and nums2):
                return []
        
            n1 = len(nums1)
            n2 = len(nums2)
        
            res = []
            q = [(nums1[0]+nums2[0],0,0)]
            visited = {}
        
            while len(res) < k and q:
            
                s, i, j = heapq.heappop(q)
                res.append(s)
            
                if i+1 < n1 and (i+1,j) not in visited:
                    heapq.heappush(q, (nums1[i+1]+nums2[j],i+1,j))
                    visited[(i+1,j)] = 1
            
                if j+1 < n2 and (i, j+1) not in visited:
                    heapq.heappush(q, (nums1[i]+nums2[j+1],i,j+1))
                    visited[(i,j+1)] = 1
        
            return res
        
        res = mat[0]
        for row in mat[1:]:
            res = kSmallestPairs(res, row)
        
        return res[k-1]
                
        