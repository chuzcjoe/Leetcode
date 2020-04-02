class Solution:
    def findLucky(self, arr: List[int]) -> int:
        

        largest = 0
        
        for i in range(len(arr)):
            if arr.count(arr[i]) == arr[i]:
                if arr[i] > largest:
                    largest = arr[i]
        
        if largest:
            return largest
        else:
            return -1
        