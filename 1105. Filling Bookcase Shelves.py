class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        
        dp = [float('inf')] * len(books)
        
        for j in range(len(books)):
            for i in range(j,-1,-1):
                W = sum([book[0] for book in books[i:j+1]])
                if W <= shelf_width:
                    H = max([book[1] for book in books[i:j+1]])
                    if i==0:
                        dp[j] = min(dp[j], 0+H)
                    else:
                        dp[j] = min(dp[j], dp[i-1]+H)
                else:
                    break

        return dp[-1]