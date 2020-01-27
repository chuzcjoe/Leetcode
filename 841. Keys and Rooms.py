class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        
        results = [False] * len(rooms)
        
        def dfs(room_num):
            if results[room_num]:
                return
            
            results[room_num] = True
            
            nums = [num for num in rooms[room_num]]
            for i in nums:
                dfs(i)
        
        dfs(0)
        
        return True if all(results) else False
        