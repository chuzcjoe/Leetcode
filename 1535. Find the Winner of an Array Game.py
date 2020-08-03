class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        
        conse_win = 0
        pre_win = None
        
        if k >= len(arr)-1:
            return max(arr)
        
        while True:
            if arr[0] > arr[1]:
                tmp = arr[1]
                arr.remove(tmp)
                arr.append(tmp)
                cur_win = arr[0]
            else:
                tmp = arr[0]
                arr.remove(tmp)
                arr.append(tmp)
                cur_win = arr[0]
            
            if cur_win == pre_win:
                conse_win += 1
            else:
                conse_win = 1
            
            pre_win = cur_win
            
            if conse_win == k:
                return arr[0]
            
            
            
            
            
            
                