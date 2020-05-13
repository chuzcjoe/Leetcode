class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        arr = sorted(arr)
        
        dic = collections.defaultdict(list)
        MIN = float('inf')
        
        for i in range(len(arr)-1):
            dic[arr[i+1]-arr[i]].append([arr[i],arr[i+1]])
            MIN = min(MIN, arr[i+1]-arr[i])
        
        return dic[MIN]