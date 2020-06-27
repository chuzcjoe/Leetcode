class Solution:
    def average(self, salary: List[int]) -> float:
        
        s = 0
        MIN = float("inf")
        MAX = -float("inf")
        
        for a in salary:
            s += a
            if a > MAX:
                MAX = a
            
            if a < MIN:
                MIN = a
        
        return (s-MAX-MIN)/(len(salary)-2)