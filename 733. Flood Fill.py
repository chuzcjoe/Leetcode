class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        
        startColor = image[sr][sc]
        
        h = len(image)
        w = len(image[0])
        
        def  bfs(image,r,c,newColor):
            image[r][c] = newColor
            directions = [[-1,0],[1,0],[0,1],[0,-1]]
            
            
            for d in directions:
                x = r + d[0]
                y = c + d[1]
                
                if x >= h or x < 0 or y < 0 or y >= w or image[x][y] == newColor:
                    continue
                
                if image[x][y] == startColor:
                    bfs(image,x,y,newColor)
                    
        
        bfs(image,sr,sc,newColor)
        
        return image