class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        
        rows = collections.defaultdict(set)
        for row in reservedSeats:
            rows[row[0]].add(row[1])
            

        res = 0
        for row in rows:
            reserved = rows[row]
            cnt = 0
            if 2 not in reserved and 3 not in reserved and 4 not in reserved and 5 not in reserved:
                cnt += 1
            
            if 6 not in reserved and 7 not in reserved and 8 not in reserved and 9 not in reserved:
                cnt += 1
            
            if 4 not in reserved and 5 not in reserved and 6 not in reserved and 7 not in reserved and cnt == 0:
                cnt += 1
            
            res += cnt

                
        
        return res + 2 * (n - len(rows))
                