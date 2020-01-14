class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        
        arr, nn, q, seen, moves = [0], len(board) ** 2, [1], set(), 0
        
        for i, row in enumerate(board[::-1]):
            if i % 2 != 0:
                arr += row[::-1]
            else:
                arr += row
        
        while q:
            new = []
            for sq in q:
                if sq == nn:
                    return moves
                for i in range(1,7):
                    if sq+i <= nn and sq+i not in seen:
                        seen.add(sq+i)
                        new.append(sq+i if arr[sq+i] == -1 else arr[sq+i])
            q, moves = new, moves + 1
        
        return -1
        