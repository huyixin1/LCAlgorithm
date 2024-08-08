class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        SR, SC = len(image), len(image[0])
        oldColor = image[sr][sc] 
        if oldColor == color:return image
        def dfs(r,c):
            if image[r][c] == oldColor:
                image[r][c] = color
                if r < SR-1: dfs(r+1,c) # up
                if r > 0: dfs(r-1,c) # down
                if c > 0:  dfs(r,c-1) # left
                if c < SC-1: dfs(r,c+1) # right
        dfs(sr,sc)
        return image