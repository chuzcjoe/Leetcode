class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        tos = set()
        
        for f,t in edges:
            tos.add(t)
            
        return list(set(list(range(n))) - tos)
        
        