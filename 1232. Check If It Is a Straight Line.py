class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        def slop(coord1, coord2):
            if coord1[0] == coord2[0]:
                return '#'
            else:
                return (coord2[1]-coord1[1]) / (coord2[0]-coord1[0])
        
        
        coord1 = coordinates[0]
        
        for i in range(1,len(coordinates)-1):
            if slop(coord1, coordinates[i]) != slop(coord1, coordinates[i+1]):
                return False
        
        return True
            